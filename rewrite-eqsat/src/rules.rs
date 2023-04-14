use egg::*;
use itertools::Itertools;

use crate::analysis::*;
use crate::language::*;
use ilog::IntLog;

fn highest_power_of_2(n: usize) -> usize {
    n & !(n-1)
}

fn var(s: &str) -> Var {
    s.parse().unwrap()
}

pub fn is_not_zero(var: &str) -> impl Fn(&mut EGraph<TensorLang, TensorAnalysis>, Id, &Subst) -> bool {
    let var = var.parse().unwrap();
    move |egraph, _, subst| {
        if let TensorData{kind, val, name: _, constant, shape: _, data: _} = &egraph[subst[var]].data {
            (*val != 0) && *constant && (*kind == DataKind::Scalar)
        } else {
            false
        }
    }
}


pub fn is_tensor(var: &str) -> impl Fn(&mut EGraph<TensorLang, TensorAnalysis>, Id, &Subst) -> bool {
    let var = var.parse().unwrap();
    move |egraph, _, subst| {
        if let TensorData{kind, val, name, constant, shape, data} = &egraph[subst[var]].data {
            *kind == DataKind::Tensor
        }else{
            false
        }
    }
}

struct SplitStackApplier{
    orig: Var,
}


impl Applier<TensorLang, TensorAnalysis> for SplitStackApplier {
    fn apply_one(
        &self,
        egraph: &mut EGraph<TensorLang, TensorAnalysis>,
        eclass: Id,
        subst: &Subst,
        searcher_ast: Option<&PatternAst<TensorLang>>,
        rule_name: Symbol,
    ) -> Vec<Id> {  
        let a_data = &egraph[eclass].data;

        if a_data.kind == DataKind::Tensor {
            let mut res = vec![];
            let shapes = a_data.shape.clone();
            for i in 1..shapes.len(){
                let dim_size = shapes[i];
                let power = highest_power_of_2(usize::try_from(dim_size).unwrap());
                let exp = power.checked_log2().unwrap();
                for c in 0..exp {
                    let power = 2_usize.pow(c.try_into().unwrap());
                    let pattern: Pattern<TensorLang> = format!("(stack (split ?a {power} {i}) {i})").parse().unwrap();
                    let mut result = pattern.apply_one(egraph, eclass, subst, searcher_ast, rule_name);

                    res.append(&mut result);
                }
            }
            res
        }else{
            vec![]
        }
    }
}

struct ExpTransposeApplier  {
    orig: Var,
}

impl Applier<TensorLang, TensorAnalysis> for ExpTransposeApplier {
    fn apply_one(
        &self,
        egraph: &mut EGraph<TensorLang, TensorAnalysis>,
        eclass: Id,
        subst: &Subst,
        searcher_ast: Option<&PatternAst<TensorLang>>,
        rule_name: Symbol,
    ) -> Vec<Id> {  
        let a_data = &egraph[eclass].data;

        if a_data.kind == DataKind::Tensor {
            let dim = a_data.shape.len().clone();
            if dim > 1 && dim <= 6 {
                let res = vec![];

                for perm in (0..dim).permutations(dim){
                    print!("{:?}\n", perm);
                }
                res
            } else {
                vec![]
            }
        }else{
            vec![]
        }
    }
}

#[rustfmt::skip]
pub fn tensat_rules() -> Vec<Rewrite<TensorLang, TensorAnalysis>> { vec![
        rewrite!("ewadd-is-associative"            ; "(ewadd ?x (ewadd ?y ?z))"                                             => "(ewadd (ewadd ?x ?y) ?z)"),
        rewrite!("ewadd-is-commutative"            ; "(ewadd ?x ?y)"                                                        => "(ewadd ?y ?x)"),
        rewrite!("ewmul-is-associative"            ; "(ewmul ?x (ewmul ?y ?z)) "                                             => "(ewmul (ewmul ?x ?y) ?z)"),
        rewrite!("ewmul-is-commutative"            ; "(ewmul ?x ?y) "                                                        => "(ewmul ?y ?x)"),
        rewrite!("distributivity-0"                ; "(ewmul (ewadd ?x ?y) ?z) "                                             => "(ewadd (ewmul ?x ?z) (ewmul ?y ?z))"),
        rewrite!("smul-is-associative"             ; "(smul (smul ?x ?y) ?w) "                                               => "(smul ?x  (smul ?y ?w))"),
        rewrite!("distributivity-1"                ; "(smul (ewadd ?x ?y) ?w) "                                              => "(ewadd (smul ?x ?w)  (smul ?y ?w))"),
        rewrite!("operator-commutativity-0"        ; "(smul (ewmul ?x ?y) ?w) "                                              => "(ewmul ?x  (smul ?y ?w))"),
        //rewrite!("transpose-is-its-own-inverse"    ; "(transpose (transpose ?x)) "                                           => "?x"),
        //rewrite!("operator-commutativity-1"        ; "(transpose (ewadd ?x ?y)) "                                            => "(ewadd (transpose ?x)  (transpose ?y))"),
        //rewrite!("operator-commutativity-2"        ; "(transpose (ewmul ?x ?y)) "                                            => "(ewmul (transpose ?x)  (transpose ?y))"),
        //rewrite!("operator-commutativity-3"        ; "(smul (transpose ?x) ?w) "                                             => "(transpose (smul ?x ?w))"),
        rewrite!("matmul-is-associative"           ; "(matmul ?x (matmul ?y ?z)) "                                           => "(matmul (matmul ?x ?y) ?z)"),
        rewrite!("matmul-is-linear-0"              ; "(smul (matmul ?x ?y) ?w) "                                             => "(matmul ?x  (smul ?y ?w))"),
        rewrite!("matmul-is-linear-1"              ; "(matmul ?x (ewadd ?y ?z)) "                                            => "(ewadd (matmul ?x ?y) (matmul ?x ?z))"),
        //rewrite!("matmul-and-transpose"            ; "(transpose (matmul ?x ?y)) "                                           => "(matmul (transpose ?y)  (transpose ?x))"),
        rewrite!("conv-is-bilinear-0"              ; "(conv2d ?sx ?sy ?p ?c (smul ?x ?w) ?y) "                               => "(conv2d ?sx ?sy ?p ?c ?x (smul ?y ?w))"),
        rewrite!("conv-is-bilinear-1"              ; "(smul (conv2d ?sx ?sy ?p 0 ?x ?y) ?w) "                            => "(conv2d ?sx ?sy ?p 0 (smul ?x ?w) ?y)"),
        rewrite!("conv-is-bilinear-2"              ; "(conv2d ?sx ?sy ?p 0 ?x (ewadd ?y ?z)) "                           => "(ewadd (conv2d ?sx ?sy ?p 0 ?x ?y) (conv2d ?sx ?sy ?p 0 ?x ?z))"),
        rewrite!("conv-is-bilinear-3"              ; "(conv2d ?sx ?sy ?p 0 (ewadd ?x ?y) ?z) "                           => "(ewadd (conv2d ?sx ?sy ?p 0 ?x ?z) (conv2d ?sx ?sy ?p 0 ?y ?z))"),
        //rewrite!("enlarge-convolution-kernel"      ; "(conv2d ?sx ?sy 0 ?c ?x ?y) "                                      => "(conv2d ?sx ?sy 0 ?c ?x (enlarge ?kx ?ky ?y))"),
        rewrite!("operator-commutativity-4"        ; "(conv2d ?sx ?sy ?p 2 ?x ?y) "                                      => "(relu (conv2d ?sx ?sy ?p 0 ?x ?y))"),
        //rewrite!("conv-with-2-applies-relu"    ; "(relu (transpose ?x)) "                                                => "(transpose (relu ?x))"),
        // rewrite!("pooling-by-conv.-with-Cpool"     ; "(conv2d ?sx ?sy ?p 0 ?x (Cpool ?kx ?ky)) "                              => "(poolavg ?kx ?ky ?sx ?sy ?p ?x)"),
        //rewrite!("const_iconv-and-const_pool"      ; "(poolavg ?kx ?ky 1 1 0 (Iconv ?kx ?ky)) "                              => "(Cpool ?kx ?ky)"),
        //rewrite!("identity-kernel"                 ; "(conv2d 1 1 0 0 ?x (Iconv ?kx ?ky)) "                               => "?x"),
        rewrite!("identity-matrix"                 ; "(matmul ?x   Imatmul ) "                                               => "?x"),
        rewrite!("ewmul-identity"                  ; "(ewmul ?x Iewmul) "                                                    => "?x"),
        //rewrite!("split-definition-0"              ; "(split_0 ?a (concat ?a ?x ?y)) "                                       => "?x"),
        //rewrite!("split-definition-1"              ; "(split_1 ?a (concat ?a ?x ?y)) "                                       => "?y"),
        rewrite!("geometry-of-concatenation"       ; "(concat 0 (concat 1 ?x ?y) (concat 1 ?z ?w)) "                         => "(concat 1 (concat 0 ?x ?z) (concat 0 ?y ?w))"),
        rewrite!("operator-commutativity-5"        ; "(concat ?a (smul ?x ?w) (smul ?y ?w)) "                                => "(smul (concat ?a ?x ?y) ?w)"),
        rewrite!("operator-commutativity-6"        ; "(concat ?a (ewadd ?x ?y) (ewadd ?z ?w)) "                              => "(ewadd (concat ?a ?x ?z) (concat ?a ?y ?w))"),
        rewrite!("operator-commutativity-7"        ; "(concat ?a (ewmul ?x ?y) (ewmul ?z ?w)) "                              => "(ewmul (concat ?a ?x ?z) (concat ?a ?y ?w))"),
        rewrite!("operator-commutativity-8"        ; "(concat ?a (relu ?x) (relu ?y)) "                                      => "(relu (concat ?a ?x ?y))"),
        //rewrite!("concatenation-and-transpose"     ; "(concat 1 (transpose ?x) (transpose ?y)) "                             => "(transpose (concat 0 ?x ?y))"),
        rewrite!("concatenation-and-matrix-mul.-0" ; "(concat 1 (matmul ?x ?y) (matmul ?x ?z)) "                             => "(matmul ?x (concat 1 ?y ?z))"),
        rewrite!("concatenation-and-matrix-mul.-1" ; "(matmul (concat 1 ?x ?z) (concat 0 ?y ?w)) "                           => "(ewadd (matmul ?x ?y) (matmul ?z ?w))"),
        rewrite!("concatenation-and-conv.-0"       ; "(concat 0 (conv2d ?sx ?sy ?p ?c ?x ?z) (conv2d ?sx ?sy ?p ?c ?y ?z)) " => "(conv2d ?sx ?sy ?p ?c (concat 0 ?x ?y) ?z)"),
        rewrite!("concatenation-and-conv.-1"       ; "(concat 1 (conv2d ?sx ?sy ?p ?c ?x ?y) (conv2d ?sx ?sy ?p ?c ?x ?z)) " => "(conv2d ?sx ?sy ?p ?c ?x (concat 0 ?y ?z))"),
        rewrite!("concatenation-and-conv.-2"       ; "(conv2d ?sx ?sy ?p 0 (concat 1 ?x ?z) (concat 1 ?y ?w)) "          => "(ewadd (conv2d ?sx ?sy ?p 0 ?x ?y) (conv2d ?sx ?sy ?p 0 ?z ?w))"),
        //rewrite!("concatenation-and-pooling-0"     ; "(concat 1 (poolavg ?kx ?ky ?sx ?sy ?p ?x) (poolavg ?kx ?ky ?sx ?sy ?p ?y)) "               => "(poolavg ?kx ?ky ?sx ?sy ?p (concat 1 ?x ?y))"),
        //rewrite!("concatenation-and-pooling-1"     ; "(concat 0 (poolmax ?kx ?ky ?sx ?sy ?p ?x) (poolmax ?kx ?ky ?sx ?sy ?p ?y)) "               => "(poolmax ?kx ?ky ?sx ?sy ?p (concat 0 ?x ?y))"),
        //rewrite!("concatenation-and-pooling-2"     ; "(concat 1 (poolmax ?kx ?ky ?sx ?sy ?p ?x) (poolmax ?kx ?ky ?sx ?sy ?p ?y)) "               => "(poolmax ?kx ?ky ?sx ?sy ?p (concat 1 ?x ?y))"),
        // inverse
        rewrite!("-ewadd-is-associative"            ;"(ewadd (ewadd ?x ?y) ?z)"                                                => "(ewadd ?x (ewadd ?y ?z)) "                                             ),
        rewrite!("-ewadd-is-commutative"            ;"(ewadd ?y ?x)"                                                           => "(ewadd ?x ?y) "                                                        ),
        rewrite!("-ewmul-is-associative"            ;"(ewmul (ewmul ?x ?y) ?z)"                                                => "(ewmul ?x (ewmul ?y ?z)) "                                             ),
        rewrite!("-ewmul-is-commutative"            ;"(ewmul ?y ?x)"                                                           => "(ewmul ?x ?y) "                                                        ),
        rewrite!("-distributivity-0"                ;"(ewadd (ewmul ?x ?z) (ewmul ?y ?z))"                                     => "(ewmul (ewadd ?x ?y) ?z) "                                             ),
        rewrite!("-smul-is-associative"             ;"(smul ?x  (smul ?y ?w))"                                                 => "(smul (smul ?x ?y) ?w) "                                               ),
        rewrite!("-distributivity-1"                ;"(ewadd (smul ?x ?w)  (smul ?y ?w))"                                      => "(smul (ewadd ?x ?y) ?w) "                                              ),
        rewrite!("-operator-commutativity-0"        ;"(ewmul ?x  (smul ?y ?w))"                                                => "(smul (ewmul ?x ?y) ?w) "                                              ),
        //rewrite!("-transpose-is-its-own-inverse"    ;"?x"                                                                      => "(transpose (transpose ?x)) "                                           ),
        //rewrite!("-operator-commutativity-1"        ;"(ewadd (transpose ?x)  (transpose ?y))"                                  => "(transpose (ewadd ?x ?y)) "                                            ),
        //rewrite!("-operator-commutativity-2"        ;"(ewmul (transpose ?x)  (transpose ?y))"                                  => "(transpose (ewmul ?x ?y)) "                                            ),
        //rewrite!("-operator-commutativity-3"        ;"(transpose (smul ?x ?w))"                                                => "(smul (transpose ?x) ?w) "                                             ),
        rewrite!("-matmul-is-associative"           ;"(matmul (matmul ?x ?y) ?z)"                                              => "(matmul ?x (matmul ?y ?z)) "                                           ),
        rewrite!("-matmul-is-linear-0"              ;"(matmul ?x  (smul ?y ?w))"                                               => "(smul (matmul ?x ?y) ?w) "                                             ),
        rewrite!("-matmul-is-linear-1"              ;"(ewadd (matmul ?x ?y) (matmul ?x ?z))"                                   => "(matmul ?x (ewadd ?y ?z)) "                                            ),
        //rewrite!("-matmul-and-transpose"            ;"(matmul (transpose ?y)  (transpose ?x))"                                 => "(transpose (matmul ?x ?y)) "                                           ),
        rewrite!("-conv-is-bilinear-0"              ;"(conv2d ?sx ?sy ?p ?c ?x (smul ?y ?w))"                                  => "(conv2d ?sx ?sy ?p ?c (smul ?x ?w) ?y) "                               ),
        rewrite!("-conv-is-bilinear-1"              ;"(conv2d ?sx ?sy ?p 0 (smul ?x ?w) ?y)"                               => "(smul (conv2d ?sx ?sy ?p 0 ?x ?y) ?w) "                            ),
        rewrite!("-conv-is-bilinear-2"              ;"(ewadd (conv2d ?sx ?sy ?p 0 ?x ?y) (conv2d ?sx ?sy ?p 0 ?x ?z))" => "(conv2d ?sx ?sy ?p 0 ?x (ewadd ?y ?z)) "                           ),
        rewrite!("-conv-is-bilinear-3"              ;"(ewadd (conv2d ?sx ?sy ?p 0 ?x ?z) (conv2d ?sx ?sy ?p 0 ?y ?z))" => "(conv2d ?sx ?sy ?p 0 (ewadd ?x ?y) ?z) "                           ),
        //rewrite!("-enlarge-convolution-kernel"      ;"(conv2d ?sx ?sy 0 ?c ?x (enlarge ?kx ?ky ?y))"                            => "(conv2d ?sx ?sy 0 ?c ?x ?y) "                                      ),
        rewrite!("-operator-commutativity-4"        ;"(relu (conv2d ?sx ?sy ?p 0 ?x ?y))"                                  => "(conv2d ?sx ?sy ?p 2 ?x ?y) "                                      ),
        //rewrite!("-conv-with-2-applies-relu"    ;"(transpose (relu ?x))"                                                   => "(relu (transpose ?x)) "                                                ),
        //rewrite!("-pooling-by-conv.-with-Cpool"     ;"(poolavg ?kx ?ky ?sx ?sy ?p ?x)"                                                   => "(conv2d ?sx ?sy ?p 0 ?x (Cpool ?kx ?ky)) "                              ),
        //rewrite!("-const_iconv-and-const_pool"      ;"(Cpool ?kx ?ky)"                              => "(poolavg ?kx ?ky 1 1 0 (Iconv ?kx ?ky))"),
        // rewrite!("-identity-kernel"                 ;"?x"                                                                      => "(conv2d 1 1 0 0 ?x (Iconv ?k)) "                               ),
        rewrite!("-identity-matrix"                 ;"?x"                                                                      => "(matmul ?x   Imatmul ) "                                               ),
        rewrite!("-ewmul-identity"                  ;"?x"                                                                      => "(ewmul ?x Iewmul) "                                                    ),
        // rewrite!("-split-definition-00"              ;"?x"                                                                      => "(split_0 1 (concat 1 ?x ?y)) "                                       ),
        // rewrite!("-split-definition-01"              ;"?x"                                                                      => "(split_0 0 (concat 0 ?x ?y)) "                                       ),
        // rewrite!("-split-definition-10"              ;"?y"                                                                      => "(split_1 0 (concat 0 ?x ?y)) "                                       ),
        // rewrite!("-split-definition-11"              ;"?y"                                                                      => "(split_1 1 (concat 1 ?x ?y)) "                                       ),
        rewrite!("-geometry-of-concatenation"       ;"(concat 1 (concat 0 ?x ?z) (concat 0 ?y ?w))"                            => "(concat 0 (concat 1 ?x ?y) (concat 1 ?z ?w)) "                         ),
        rewrite!("-operator-commutativity-5"        ;"(smul (concat ?a ?x ?y) ?w)"                                             => "(concat ?a (smul ?x ?w) (smul ?y ?w)) "                                ),
        rewrite!("-operator-commutativity-6"        ;"(ewadd (concat ?a ?x ?z) (concat ?a ?y ?w))"                             => "(concat ?a (ewadd ?x ?y) (ewadd ?z ?w)) "                              ),
        rewrite!("-operator-commutativity-7"        ;"(ewmul (concat ?a ?x ?z) (concat ?a ?y ?w))"                             => "(concat ?a (ewmul ?x ?y) (ewmul ?z ?w)) "                              ),
        rewrite!("-operator-commutativity-8"        ;"(relu (concat ?a ?x ?y))"                                                => "(concat ?a (relu ?x) (relu ?y)) "                                      ),
        //rewrite!("-concatenation-and-transpose"     ;"(transpose (concat 0 ?x ?y))"                                            => "(concat 1 (transpose ?x) (transpose ?y)) "                             ),
        rewrite!("-concatenation-and-matrix-mul.-0" ;"(matmul ?x (concat 1 ?y ?z))"                                            => "(concat 1 (matmul ?x ?y) (matmul ?x ?z)) "                             ),
        rewrite!("-concatenation-and-matrix-mul.-1" ;"(ewadd (matmul ?x ?y) (matmul ?z ?w))"                                   => "(matmul (concat 1 ?x ?z) (concat 0 ?y ?w)) "                           ),
        rewrite!("-concatenation-and-conv.-0"       ;"(conv2d ?sx ?sy ?p ?c (concat 0 ?x ?y) ?z)"                              => "(concat 0 (conv2d ?sx ?sy ?p ?c ?x ?z) (conv2d ?sx ?sy ?p ?c ?y ?z)) " ),
        rewrite!("-concatenation-and-conv.-1"       ;"(conv2d ?sx ?sy ?p ?c ?x (concat 0 ?y ?z))"                              => "(concat 1 (conv2d ?sx ?sy ?p ?c ?x ?y) (conv2d ?sx ?sy ?p ?c ?x ?z)) " ),
        rewrite!("-concatenation-and-conv.-2"       ;"(ewadd (conv2d ?sx ?sy ?p 0 ?x ?y) (conv2d ?sx ?sy ?p 0 ?z ?w))" => "(conv2d ?sx ?sy ?p 0 (concat 1 ?x ?z) (concat 1 ?y ?w)) "          ),
        //rewrite!("-concatenation-and-pooling-0"     ;"(poolavg ?kx ?ky ?sx ?sy ?p (concat 1 ?x ?y))"                                     => "(concat 1 (poolavg ?kx ?ky ?sx ?sy ?p ?x) (poolavg ?kx ?ky ?sx ?sy ?p ?y)) "               ),
        //rewrite!("-concatenation-and-pooling-1"     ;"(poolmax ?kx ?ky ?sx ?sy ?p (concat 0 ?x ?y))"                                     => "(concat 0 (poolmax ?kx ?ky ?sx ?sy ?p ?x) (poolmax ?kx ?ky ?sx ?sy ?p ?y)) "               ),
        //rewrite!("-concatenation-and-pooling-2"     ;"(poolmax ?kx ?ky ?sx ?sy ?p (concat 1 ?x ?y))"                                     => "(concat 1 (poolmax ?kx ?ky ?sx ?sy ?p ?x) (poolmax ?kx ?ky ?sx ?sy ?p ?y)) "               ),
]}

#[rustfmt::skip]
pub fn split_rules() -> Vec<Rewrite<TensorLang, TensorAnalysis>> { vec![
    rewrite!("exp-split-stack"; "?a" =>  { SplitStackApplier {orig: var("?a") } } ),
    rewrite!("stack-matmul"; "(stack (list (matmul ?a ?b) (matmul ?c ?d)) ?dim)" => "(matmul (stack (list ?a ?c) ?dim) (stack (list ?b ?d) ?dim))"),
    rewrite!("stack-matmul2"; "(matmul (stack (list ?a ?c) ?dim) (stack (list ?b ?d) ?dim))" => "(stack (list (matmul ?a ?b) (matmul ?c ?d)) ?dim)"),
    rewrite!("exp-transpose"; "?a" => { ExpTransposeApplier {orig: var("?a")} }),
]}


#[rustfmt::skip]
pub fn scalar_rules() -> Vec<Rewrite<TensorLang, TensorAnalysis>> { vec![
    rewrite!("comm-add";  "(+ ?a ?b)"        => "(+ ?b ?a)"),
    rewrite!("comm-mul";  "(* ?a ?b)"        => "(* ?b ?a)"),
    rewrite!("assoc-add"; "(+ ?a (+ ?b ?c))" => "(+ (+ ?a ?b) ?c)"),
    rewrite!("assoc-mul"; "(* ?a (* ?b ?c))" => "(* (* ?a ?b) ?c)"),
    
    rewrite!("dist-mul"; "(* ?a (+ ?b ?c))" => "(+ (* ?a ?b) (* ?a ?c))"), 

    rewrite!("sub-canon"; "(- ?a ?b)" => "(+ ?a (* -1 ?b))"),
    rewrite!("canon-sub"; "(+ ?a (* -1 ?b))"   => "(- ?a ?b)"),

    rewrite!("zero-add"; "(+ ?a 0)" => "?a"),
    rewrite!("zero-mul"; "(* ?a 0)" => "0"),
    rewrite!("one-mul";  "(* ?a 1)" => "?a"),
    rewrite!("one-div"; "(// ?a 1)" => "?a"),
    
    rewrite!("cancel-sub"; "(- ?a ?a)" => "0"),
    rewrite!("cancel-div"; "(// ?a ?a)" => "1" if is_not_zero("?a"))
]}

#[rustfmt::skip]
pub fn scalar_rules_exploratory() -> Vec<Rewrite<TensorLang, TensorAnalysis>> { vec![
    rewrite!("add-zero"; "?a" => "(+ ?a 0)"),
    rewrite!("mul-one";  "?a" => "(* ?a 1)"),
]}



pub fn all_rules() ->  Vec<Rewrite<TensorLang, TensorAnalysis>> {
    let mut all_rules = vec![];
    all_rules.extend(scalar_rules());
    all_rules.extend(split_rules());

    return all_rules;
}


#[cfg(test)]
mod tests {

    use super::*;
    test_fn! {
        comm_add, 
        scalar_rules(), 
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(+ a 1)" => "(+ 1 a)"
    }


    test_fn!{
        comm_arith, 
        scalar_rules(),
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(* a (+ b c))" => "(+ (* a b) (* a c))", "(* (+ b c) a)" 
    }


    test_fn! {
        add_zero, 
        scalar_rules(), 
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(+ a 0)" => "(+ 0 a)", "a"
    }


    test_fn! {
        cancel_div, 
        scalar_rules(), 
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(// 5 5)" => "1"
    }


    test_fn! {
        complex_arith, 
        scalar_rules(), 
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(+ (// 5 (+ 1 (* 0 5))) (* (+ c a) 0))" => "5"
    }

    /* 
    test_fn!{
        split_1,
        split_rules(),
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(tensor test (shape 1 2 3))" => "(stack (split (tensor test (shape 1 2 3)) 1 1) 1)"
    }

    test_fn!{
        split_2,
        split_rules(),
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(tensor test (shape 1 4 3))" => "(stack (split (tensor test (shape 1 4 3)) 2 1) 1)"
    }*/

    test_fn!{
        tensat,
        tensat_rules(),
        runner = Runner::<TensorLang, TensorAnalysis>::default(),
        "(ewadd (tensor test (shape 1 4 3)) (tensor test2 (shape 1 4 3)))" => "(ewadd (tensor test2 (shape 1 4 3)) (tensor test (shape 1 4 3)))"
    }
}