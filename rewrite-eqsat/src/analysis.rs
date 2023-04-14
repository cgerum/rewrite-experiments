#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unused_imports)]

use std::collections::HashSet;

use egg::{Analysis, DidMerge, EGraph, Id, RecExpr};

use ndarray::{ArrayD, Data};

use crate::language::{TensorLang};


#[derive(Debug, PartialEq, Clone, Copy)]
pub enum DataKind {
    None,
    Symbol, //Name
    Scalar,
    Tensor, //Tnsr
    Shape, 
    List,   
    TensorTuple, //FIXME: Check if replaceable by list
}


impl Default for DataKind {
    fn default() -> Self {
        DataKind::None
    }
}

/// Metadata struct for TensorAnalysis
#[derive(Debug, Clone)]
pub struct TensorData {
    /// The data type of this eclass, can be a name/scalar/tensor
    pub kind: DataKind, //dtype
    /// The value of this eclass if it is a Scalar type
    pub val: i64,
    /// The name string of this eclass if it is a Name type
    pub name: String,
    /// If the tensor results from all constant computations
    pub constant: bool, // constant
    /// Shape if it is a shape or tensor type
    pub shape: Vec<i64>,
    /// Data 
    pub data: Option<ArrayD<i64>>, //FIXME: allow symbolic values
}


impl Default for TensorData {
    fn default() -> Self {
        TensorData {
            kind: DataKind::None,
            val: 0,
            name: String::from(""),
            constant: false,
            shape: Vec::default(),
            data: None,
        }
    }
}


/// Struct for metadata analysis
///
/// In this analysis, it calls functions on the TASO side (e.g. graph.matmul())
/// to create (or get) new ops/nodes and stores pointers to the output tensors.
/// TASO will measure and store the runtime cost when creating a new op/node.
#[derive(Default)]
pub struct TensorAnalysis{
}

impl Analysis<TensorLang> for TensorAnalysis {
    type Data = TensorData;

    // Constructs metadata for a new enode
    fn make(egraph: &EGraph<TensorLang, Self>, enode: &TensorLang) -> Self::Data {
        let x = |i: &Id| &egraph[*i].data;

        match enode {
            TensorLang::List(values) => {
                let mut lst : Vec<i32> = Vec::default();

                for elem in values.iter() {
                    let data = x(elem);
                    if data.kind == DataKind::Scalar {
                        lst.push(data.val.try_into().unwrap());
                    }
                }

                Self::Data{
                    kind: DataKind::Shape,
                    data: None, // FIXME: extract dataSome(ArrayD::from(lst)),
                    ..Default::default()
                }
            }

            TensorLang::Shape(shape) => {

                let mut s : Vec<i64> = Vec::default();

                for elem in shape.iter() {
                    let data = x(elem);
                    assert!(data.kind == DataKind::Scalar);
                    assert!(data.constant == true);
                    s.push(data.val.try_into().unwrap());
                }


                Self::Data{
                    kind: DataKind::Shape,
                    shape: s,
                    ..Default::default()
                }
            }

            TensorLang::Tensor([name_id, shape_id]) => {
                let name_data = x(name_id);
                let shape_data = x(shape_id);
                
                assert!(name_data.kind == DataKind::Symbol);
                assert!(shape_data.kind == DataKind::Shape);

                Self::Data{
                    kind: DataKind::Tensor,
                    name: name_data.name.clone(),
                    constant: false,
                    shape: shape_data.shape.clone(),
                    ..Default::default()
                }
            }

            TensorLang::Const([name_id, shape_id]) => {
                let name_data = x(name_id);
                let shape_data = x(shape_id);
                
                assert!(name_data.kind == DataKind::Symbol);
                assert!(shape_data.kind == DataKind::Shape);

                Self::Data{
                    kind: DataKind::Tensor,
                    name: name_data.name.clone(),
                    constant: true,
                    shape: shape_data.shape.clone(),
                    ..Default::default()
                }
            }

            TensorLang::Matmul([a_id, b_id]) => {
                // Check types
                let a_data = x(a_id);
                let b_data = x(b_id);
                
                // FIXME: this should work
                //assert!(a_data.kind == DataKind::Tensor);
                //assert!(b_data.kind == DataKind::Tensor);
                
                // Get arguments
                let constant = a_data.constant && b_data.constant;

                // Create tensorhandle and get metadata
                Self::Data {
                    kind: DataKind::Tensor,
                    constant: constant,
                    //shape: vec![a_data.shape[0], b_data.shape[1]],
                    ..Default::default()
                }
            }

            // assuming NHWC and OIHW
            TensorLang::Conv2d([stride_h, stride_w, pad, dilation, inpt, wght]) => {
                // Check types
                assert!(x(stride_h).kind == DataKind::Scalar);
                assert!(x(stride_w).kind == DataKind::Scalar);
                assert!(x(pad).kind == DataKind::Scalar);
                assert!(x(inpt).kind == DataKind::Tensor);
                assert!(x(wght).kind == DataKind::Tensor);
                assert!(x(dilation).kind == DataKind::Scalar);

                // Get arguments
                let strideH = x(stride_h).val;
                let strideW = x(stride_w).val;
                let constant = x(inpt).constant && x(wght).constant;

                let output_shape = vec![x(inpt).shape[0], ((x(inpt).shape[1] + 2 * x(pad).val) - (x(wght).shape[2]/2)) / x(stride_h).val , ((x(inpt).shape[2] + 2 * x(pad).val) - (x(wght).shape[3]/2)) / x(stride_w).val , x(wght).shape[0]];

                // Create tensorhandle and get metadata
                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    shape: output_shape,
                    ..Default::default()
                }
            }

            TensorLang::Concatenate(params) => {
                // Check types
                let dim = x(&params[0]);
                let tensor_list = &params[1..];
                assert!(dim.kind == DataKind::Scalar);

                let mut base_shape = x(&tensor_list[0]).shape.clone();
                let mut out_shape = 0;
                for elem in tensor_list.iter() {
                    let data = x(elem);
                    assert!(data.kind == DataKind::Tensor);
                    assert!(data.shape.len() == base_shape.len());

                    let mut inx:usize = 0;
                    for i in data.shape.iter() {
                        if inx == dim.val as usize { out_shape += *i; }
                        else {assert!(base_shape[inx] == *i);}
                        inx += 1 as usize;
                    }
                }
                base_shape[dim.val as usize] = out_shape;


                // create tensorhandle and get metadata
                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    shape: base_shape,
                    ..Default::default()
                }
            }

 
            TensorLang::Elementwise([func, a]) => {
                assert!(x(a).kind == DataKind::Tensor);
                let constant = x(a).constant;

                
                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Int(_n) => Self::Data {
                kind: DataKind::Scalar,
                val: *_n,
                name: String::new(),
                constant: true,
                ..Default::default()
            },
            TensorLang::UInt(_n) => Self::Data {
                kind: DataKind::Scalar,
                val: *_n as i64, //FIXME: make analysis type sensitive
                name: String::new(),
                constant: true,
                ..Default::default()
            },

            TensorLang::Symbol(_s) => Self::Data {
                kind: DataKind::Symbol,
                val: 0,
                name: _s.as_str().to_string(),
                constant: false,
                ..Default::default()
            },

            TensorLang::Add([a, b]) => {
                let mut data : Self::Data = Default::default();
                data.kind = DataKind::Scalar;
                data
            }

            TensorLang::Sub([a, b]) => {
                let mut data : Self::Data = Default::default();
                data.kind = DataKind::Scalar;
                data
            }

            TensorLang::Mul([a, b]) => {
                let mut data : Self::Data = Default::default();
                data.kind = DataKind::Scalar;
                data
            }

            TensorLang::CeilDiv([a, b]) => {
                let mut data : Self::Data = Default::default();
                data.kind = DataKind::Scalar;
                data
            }

            
            TensorLang::CeilRem([a, b]) => {
                let mut data : Self::Data = Default::default();
                data.kind = DataKind::Scalar;
                data
            }

            TensorLang::Extern(args) => {
                Self::Data::default()
            }

            TensorLang::Pow([val, exp]) => {
                Self::Data::default()
            }

            TensorLang::Ewadd([a, b]) => {
                // Check types
                assert!(x(a).kind == DataKind::Tensor);
                assert!(x(b).kind == DataKind::Tensor);

                // Get arguments
                let constant = x(a).constant && x(b).constant;
                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Ewmul([a, b]) => {
                // Check types
                //assert!(x(a).kind == DataKind::Tensor);
                //assert!(x(b).kind == DataKind::Tensor);

                // Get arguments
                let constant = x(a).constant && x(b).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Transpose([inpt, perm_name, shuffle]) => {
                // Check types
                assert!(x(perm_name).kind == DataKind::Symbol);
                assert!(x(inpt).kind == DataKind::Tensor);
                assert!(x(shuffle).kind == DataKind::Scalar);

                // Get arguments
                let perms: Vec<i32> = x(perm_name)
                    .name
                    .split("_")
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect();
                let shuffle_val = x(shuffle).val;
                let constant = x(inpt).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }


            TensorLang::Enlarge([a, b]) => {
                // Check types
                assert!(x(a).kind == DataKind::Tensor);
                assert!(x(b).kind == DataKind::Tensor);

                // Get arguments
                let constant = x(a).constant && x(b).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Dropout(a) => {
                assert!(x(a).kind == DataKind::Tensor);
                let constant = x(a).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            
            TensorLang::Relu(a) => {
                assert!(x(a).kind == DataKind::Tensor);
                let constant = x(a).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Tanh(a) => {
                assert!(x(a).kind == DataKind::Tensor);
                let constant = x(a).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Sigmoid(a) => {
                assert!(x(a).kind == DataKind::Tensor);
                let constant = x(a).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            
            TensorLang::Poolmax([inpt, kernel_h, kernel_w, stride_h, stride_w, pad, act]) => {
                // Check types
                assert!(x(kernel_h).kind == DataKind::Scalar);
                assert!(x(kernel_w).kind == DataKind::Scalar);
                assert!(x(stride_h).kind == DataKind::Scalar);
                assert!(x(stride_w).kind == DataKind::Scalar);
                assert!(x(pad).kind == DataKind::Scalar);
                assert!(x(act).kind == DataKind::Scalar);
                assert!(x(inpt).kind == DataKind::Tensor);

                // Get arguments
                let kernelH = x(kernel_h).val;
                let kernelW = x(kernel_w).val;
                let strideH = x(stride_h).val;
                let strideW = x(stride_w).val;
                let padding = x(pad).val;
                let activation = x(act).val;
                let constant = x(inpt).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Poolavg([inpt, kernel_h, kernel_w, stride_h, stride_w, pad, act]) => {
                // Check types
                assert!(x(kernel_h).kind == DataKind::Scalar);
                assert!(x(kernel_w).kind == DataKind::Scalar);
                assert!(x(stride_h).kind == DataKind::Scalar);
                assert!(x(stride_w).kind == DataKind::Scalar);
                assert!(x(pad).kind == DataKind::Scalar);
                assert!(x(act).kind == DataKind::Scalar);
                assert!(x(inpt).kind == DataKind::Tensor);

                // Get arguments
                let kernelH = x(kernel_h).val;
                let kernelW = x(kernel_w).val;
                let strideH = x(stride_h).val;
                let strideW = x(stride_w).val;
                let padding = x(pad).val;
                let activation = x(act).val;
                let constant = x(inpt).constant;

                // Create tensorhandle and get metadata
                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            
            TensorLang::Split([axis, inpt]) => {
                // Check types
                assert!(x(axis).kind == DataKind::Scalar);
                assert!(x(inpt).kind == DataKind::Tensor);

                // Get arguments
                let axis_val = x(axis).val;
                let constant = x(inpt).constant;

                    Self::Data {
                        kind: DataKind::TensorTuple,
                        val: 0,
                        name: String::new(),
                        constant: constant,
                        ..Default::default()
                    }
                }
    

            TensorLang::Split0(inpt) => {
                // Check types
                assert!(x(inpt).kind == DataKind::TensorTuple);
                let constant = x(inpt).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Split1(inpt) => {
                // Check types
                assert!(x(inpt).kind == DataKind::TensorTuple);
                let constant = x(inpt).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }


            TensorLang::Merge([weight, count]) => {
                // Check types
                assert!(x(count).kind == DataKind::Scalar);
                assert!(x(weight).kind == DataKind::Tensor);

                // Get arguments
                let count_val = x(count).val;
                let constant = x(weight).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Reshape([inpt, shape_name]) => {
                // Check types
                assert!(x(shape_name).kind == DataKind::Symbol);
                assert!(x(inpt).kind == DataKind::Tensor);

                // Get arguments
                let dims: Vec<i32> = x(shape_name)
                    .name
                    .split("_")
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect();
                let constant = x(inpt).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Noop([a, b]) => {
                // Check types
                assert!(x(a).kind == DataKind::Tensor);
                assert!(x(b).kind == DataKind::Tensor);
                let constant = x(a).constant && x(b).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }
            
            TensorLang::BatchNorm([input, scale, bias, mean, var]) => {
                // Check types
                assert!(x(input).kind == DataKind::Tensor);
                assert!(x(scale).kind == DataKind::Tensor);
                assert!(x(bias).kind == DataKind::Tensor);
                assert!(x(mean).kind == DataKind::Tensor);
                assert!(x(var).kind == DataKind::Tensor);

                // Get arguments
                let constant = x(input).constant && x(scale).constant && x(bias).constant && x(mean).constant && x(var).constant;

                Self::Data {
                    kind: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            },
            other => {
                println!("{:?}", other);
                todo!()
            }
        }
    }

    /// Merges two metadata when two eclasses are merged.
    fn merge(&mut self, to: &mut Self::Data, from: Self::Data) -> DidMerge {
        if from.constant && (!to.constant) {
             to.constant = from.constant;
             DidMerge(true, true)
         } else {
             DidMerge(false,false)
        }
    }

    // Not needed to modify anything
    fn modify(egraph: &mut EGraph<TensorLang, Self>, id: Id) {}
}



#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_symbol() {
        let expr : RecExpr<TensorLang> = "n".parse().unwrap();

        let mut graph : EGraph::<TensorLang, TensorAnalysis> = Default::default();

        let id = graph.add_expr(&expr);
        graph.rebuild();

    }

    #[test]
    fn test_constant(){
        let expr: RecExpr<TensorLang> = "1".parse().unwrap();
        let mut graph: EGraph::<TensorLang, TensorAnalysis> = Default::default();

        let id = graph.add_expr(&expr);
        graph.rebuild();

        let data = &graph[id].data;
        assert!(data.kind == DataKind::Scalar);
        assert!(data.val == 1);
    }

    #[test]
    fn test_concatenate(){
        let expr: RecExpr<TensorLang> = "(concat 1 (tensor a (shape 1 2 3)) (tensor b (shape 1 2 3)))".parse().unwrap();
        let mut graph: EGraph::<TensorLang, TensorAnalysis> = Default::default();


        let id = graph.add_expr(&expr);
        graph.rebuild();

        let data = &graph[id].data;
        assert!(data.kind == DataKind::Tensor);
        assert!(data.shape[0] == 1);
        assert!(data.shape[1] == 4);
        assert!(data.shape[2] == 3);
    }
}