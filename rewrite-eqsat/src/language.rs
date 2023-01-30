#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unconditional_recursion)]


use egg::*;

define_language! {
    pub enum TensorLang {
        "list"      = List(Box<[Id]>),    // Represents a variable length list
        "shape"     = Shape(Box<[Id]>),   // Takes a variable length list for shapes
        "tensor"    = Tensor([Id; 2]),     // takes a Symbol and a Shape, format: name, shape    
        "const"     = Const([Id; 2]),      // takes a Symbol and a Shape, format : name, shape
        "transpose" = Transpose([Id; 2]),  // input, list of axis in order after tranposition
        "split"     = Split([Id; 3]),      // Split a tensor into a list of tensors, input, chunksize: scalar (or list of scalars), dim, scalar
        "stack"     = Stack([Id; 2]),      // Stack a list of tensors a long a dimensions: list, dim, 

        // TODO (cgerum): try to further generalize operator descriptions
        // TODO (cgerum): generalized layout transform
        // "layout"    = Layout([Id; 3]),    // input, list of symbols of lenght, list of affine expressions
        // Maybe it makes sense to have "view" as a seperate memory layout transform to explicitly 
        // describe memory transforms that change the "view" of the memory without actually copying data 
        
        // TODO (cgerum); generalized compute on tensors
        // Do we really w
        // "compute"    = Compute([ID; 3])

        //Scalar Expression
        "+"         = Add([Id; 2]),
        "-"         = Sub([Id; 2]),
        "*"         = Mul([Id; 2]),
        "//"        = CeilDiv([Id; 2]),
        "%"         = CeilRem([Id; 2]),
        "pow"       = Pow([Id; 2]),

        //FIXME these should get promoted to linear to some kind of external function calls
        "matmul"    = Matmul([Id; 2]),    // input1, input2
        "conv2d"    = Conv2d([Id; 6]),    // Conv2d
        "concat"    = Concatenate(Box<[Id]>),
        "elementwise" = Elementwise([Id; 2]), // Function, input
        Num(i32),
        Symbol(Symbol),
    }
}


#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_expr() {
        let shape_expr : RecExpr<TensorLang> = "(shape 1 2 3 4 5)".parse().unwrap();
        let input_expr : RecExpr<TensorLang> = "(tensor test (shape 1 2))".parse().unwrap();
        let weight_expr : RecExpr<TensorLang> = "(const test (shape 1 2))".parse().unwrap();
    }


    #[test]
    fn test_parse_expr() {
        let conv_expr : RecExpr<TensorLang> = "(conv2d 1 1 0 0 (tensor i1 (shape 1 2 3 2)) (const w1 (shape 2 2 3 3)))".parse().unwrap();

        let mut graph : EGraph::<TensorLang, ()> = Default::default();

        graph.add_expr(&conv_expr);
        graph.rebuild();
    }

    #[test]
    fn test_parse_ewise(){
        let expr : RecExpr<TensorLang> = "(elementwise sigmoid a)".parse().unwrap();

        let mut graph : EGraph::<TensorLang, ()> = Default::default();

        graph.add_expr(&expr);
        graph.rebuild();
    }
}