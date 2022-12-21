use egg::*;
use ndarray::Data;
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
pub fn split_rules() -> Vec<Rewrite<TensorLang, TensorAnalysis>> { vec![
    rewrite!("exp-split-stack"; "?a" =>  { SplitStackApplier {orig: var("?a") } } ),
    rewrite!("stack-matmul"; "(stack (list (matmul ?a ?b) (matmul ?c ?d)) ?dim)" => "(matmul (stack (list ?a ?c) ?dim) (stack (list ?b ?d) ?dim))"),
    rewrite!("stack-matmul"; "(matmul (stack (list ?a ?c) ?dim) (stack (list ?b ?d) ?dim))" => "(stack (list (matmul ?a ?b) (matmul ?c ?d)) ?dim)"),
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
    
    rewrite!("add-zero"; "?a" => "(+ ?a 0)"),
    rewrite!("mul-one";  "?a" => "(* ?a 1)"),

    rewrite!("cancel-sub"; "(- ?a ?a)" => "0"),
    rewrite!("cancel-div"; "(// ?a ?a)" => "1" if is_not_zero("?a"))
]}


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
}