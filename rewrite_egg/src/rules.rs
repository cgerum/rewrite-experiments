use egg::*;

use crate::analysis::*;
use crate::language::*;


pub fn is_not_zero(var: &str) -> impl Fn(&mut EGraph<TensorLang, TensorAnalysis>, Id, &Subst) -> bool {
    let var = var.parse().unwrap();
    move |egraph, _, subst| {
        if let TensorData{kind, val, name, constant, shape, data} = &egraph[subst[var]].data {
            (*val != 0) && *constant && (*kind == DataKind::Scalar)
        } else {
            false
        }
    }
}

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