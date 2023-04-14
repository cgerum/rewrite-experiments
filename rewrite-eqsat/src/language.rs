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
        //"transpose" = Transpose([Id; 2]),  // input, list of axis in order after transposition (for now use TENSATs implementation)
        //"split"     = Split([Id; 3]),      // Split a tensor into a list of tensors, input, chunksize: scalar (or list of scalars), dim, scalar
        //"stack"     = Stack([Id; 2]),      // Stack a list of tensors along a dimensions: list, dim, 

        // TODO (cgerum): try to further generalize operator descriptions
        // TODO (cgerum): generalized layout transform
        // "layout"    = Layout([Id; 3]),    // input, list of symbols of lenght, list of affine expressions
        // Maybe it makes sense to have "view" as a seperate memory layout transform to explicitly 
        // describe memory transforms that change the "view" of the memory without actually copying data 
        // TODO (cgerum); generalized compute on tensors
        // Do we really want to have such a generic compute
        // "compute"    = Compute([ID; 3])

        //Scalar Expression
        "+"         = Add([Id; 2]),
        "-"         = Sub([Id; 2]),
        "*"         = Mul([Id; 2]),
        "//"        = CeilDiv([Id; 2]),
        "%"         = CeilRem([Id; 2]),
        "pow"       = Pow([Id; 2]),

        //FIXME these should get promoted to linear or to some kind of external function calls
        "matmul"    = Matmul([Id; 2]),    // input1, input2
        "conv2d"    = Conv2d([Id; 6]),    // cnv2d: stride_h, stride_w, pad, dilation, inpt, wght
        "concat"    = Concatenate(Box<[Id]>),
        "elementwise" = Elementwise([Id; 2]), // Function, input
        "extern" = Extern(Box<[Id]>), // An external function call (represents for example a relay function)

        //Legacy Tensat Functions
        "ewadd"     = Ewadd([Id; 2]), // Elementwise ADD
        "ewmul"     = Ewmul([Id; 2]), // Elementwise MUL
        "smul"      = Smul([Id; 2]),  // Currently Unused (Tensor * Scalar)
        "transpose" = Transpose([Id; 3]), // input, perm_name (format: dim1_dim2...), shuffle
        //"matmul"    = Matmul([Id; 3]), // activation, input1, input2
        //"conv2d"    = Conv2d([Id; 6]), // conv2d's weight tensor kernel size can not be even, it seems that TASO's output shape computation is incorrect for even kernal size (like 4x4)
  
        "enlarge"   = Enlarge([Id; 2]), // input_to_enlarge, ref_input : Enlarge the third and forth dimension of input_to_enlarge to the same size as reg_input used to zero pad the kernel of the smaller conv when fusing parallel
        "dropout"   = Dropout(Id), 
        "relu"      = Relu(Id),
        "tanh"      = Tanh(Id),
        "sigmoid"   = Sigmoid(Id),
        "poolmax"   = Poolmax([Id; 7]), // input, kernel_h, kernel_w, stride_h, stride_w, padding, activation
        "poolavg"   = Poolavg([Id; 7]), // input, kernel_h, kernel_w, stride_h, stride_w, padding, activation
        //"concat"    = Concat([Id; 4]), // axis, ndim, input1, input2. ndim is for using in CheckApply only
        //"concat3"    = Concat3([Id; 5]), // axis, ndim, input1, input2. input3, ndim is for using in CheckApply only
        //"concat4"    = Concat4([Id; 6]), // axis, ndim, input1, input2. input3, input4, ndim is for using in CheckApply only
        //"concat5"    = Concat5([Id; 7]), // axis, ndim, input1, input2, input3, input4, input5. ndim is for using in CheckApply only
        // Add a concat for each number of inputs if needed
        "split_0"   = Split0(Id), // must take a split node as input
        "split_1"   = Split1(Id), // must take a split node as input
        "split"     = Split([Id; 2]), // axis, input
        //"Cpool"     = Cpool([Id; 2]),
        //"Iconv"     = Iconv([Id; 2]),
        //"Imatmul"   = Imatmul,
        //"Iewmul"    = Iewmul,
        "merge"     = Merge([Id; 2]), // merge_gconv, takes [weight, count]
        "reshape"   = Reshape([Id; 2]), // input, shape_name (format: dim1_dim2...)
        "noop"      = Noop([Id; 2]), // No op, use to combine the outputs of a graph in case there are multiple, since egg works with single root graph
        "batchnorm" = BatchNorm([Id; 5]), // input, scale, bias, mean, var 

        Int(i64),
        UInt(u64),
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

        let i = 1;
        let i2: u32 = i;
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