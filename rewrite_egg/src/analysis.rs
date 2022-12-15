#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unused_imports)]

use std::collections::HashSet;

use egg::{Analysis, DidMerge, EGraph, Id, RecExpr};

use crate::language::{TensorLang};


#[derive(Debug, PartialEq, Clone, Copy)]
pub enum DataKind {
    None,
    Symbol,
    Scalar,
    Tensor,
    Shape, 
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
    pub kind: DataKind,
    /// The value of this eclass if it is a Scalar type
    pub val: i32,
    /// The name string of this eclass if it is a Name type
    pub name: String,
    /// If the tensor results from all constant computations
    pub constant: bool,
    /// Shape if it is a shape or tensor type
    pub shape: Vec<i32>,
}

impl Default for TensorData {
    fn default() -> Self {
        TensorData {
            kind: DataKind::None,
            val: 0,
            name: String::from(""),
            constant: false,
            shape: Vec::default(),
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

    // Constructs metadata for a new enode, using TASO side functions for tensors.
    fn make(egraph: &EGraph<TensorLang, Self>, enode: &TensorLang) -> Self::Data {
        let x = |i: &Id| &egraph[*i].data;

        match enode {
            TensorLang::Shape(shape) => {

                let mut s : Vec<i32> = Vec::default();

                for elem in shape.iter() {
                    let data = x(elem);
                    assert!(data.kind == DataKind::Scalar);
                    assert!(data.constant == true);
                    s.push(data.val);
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
                    name: name_data.name,
                    constant: false,
                    shape: shape_data.shape,
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
                    name: name_data.name,
                    constant: true,
                    shape: shape_data.shape,
                    ..Default::default()
                }
            }

            TensorLang::Matmul([a_id, b_id]) => {
                // Check types
                let a_data = x(a);
                let b_data = x(b);
                assert!(a_data.kind == DataKind::Tensor)
                assert!(b_data.kind == DataKind::Tensor)
                
                // Get arguments
                let constant = a_data.constant && b_data.constant;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tensor,
                    name: String::new(),
                    contant: constant,
                    ..Default::default()
                }
            }

            TensorLang::Conv2d([stride_h, stride_w, pad, act, inpt, wght]) => {
                // Check types
                assert!(x(stride_h).dtype == DataKind::Scalar);
                assert!(x(stride_w).dtype == DataKind::Scalar);
                assert!(x(pad).dtype == DataKind::Scalar);
                assert!(x(act).dtype == DataKind::Scalar);
                assert!(x(inpt).dtype == DataKind::Tnsr);
                assert!(x(wght).dtype == DataKind::Tnsr);

                // Get arguments
                let strideH = x(stride_h).val;
                let strideW = x(stride_w).val;
                let constant = constant;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tensor,
                    val: 0,
                    name: String::new(),
                    constant: constant,
                    ..Default::default()
                }
            }

 
            TensorLang::Sigmoid(a) => {
                assert!(x(a).dtype == DataKind::Tnsr);
                let all_weights = x(a).all_weights;

                
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                    ..Default::default()
                }
            }

            TensorLang::Input([name, shape]) => {
                // Check types
                assert!(x(name).dtype == DataKind::Name);

                // Get arguments
                let mut dims = x(shape).shape.to_vec();
                let ndim = dims.len();
                dims.shrink_to_fit();
                assert!(dims.len() == dims.capacity());
                let ptr = dims.as_mut_ptr();
                std::mem::forget(dims);

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: false,
                    ..Default::default()
                }
            }

            TensorLang::Weight([name, shape]) => {
                // Check types
                assert!(x(name).dtype == DataKind::Name);

                // Get arguments
                let mut dims = x(shape).shape.to_vec();
                let ndim = dims.len();
                dims.shrink_to_fit();
                assert!(dims.len() == dims.capacity());

                let num_entries = dims.iter().product();
                let mut weight_data: Vec<f32> = (0..num_entries).map(|_| rand::random()).collect();
                weight_data.shrink_to_fit();
                assert!(weight_data.len() == weight_data.capacity());

                let ptr = dims.as_mut_ptr();
                std::mem::forget(dims);
                let data_ptr = weight_data.as_mut_ptr();
                std::mem::forget(weight_data);

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: true,
                    ..Default::default()
                }
            }

            TensorLang::Transpose([inpt, perm_name, shuffle]) => {
                // Check types
                assert!(x(perm_name).dtype == DataKind::Name);
                assert!(x(inpt).dtype == DataKind::Tnsr);
                assert!(x(shuffle).dtype == DataKind::Scalar);

                // Get arguments
                let perms: Vec<i32> = x(perm_name)
                    .name
                    .split("_")
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect();

                let shuffle_val = x(shuffle).val;
                let shuffle_bool = shuffle_val == 1;
                let all_weights = x(inpt).all_weights;

                
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                    ..Default::default()
                }
            }*/

            TensorLang::Num(_n) => Self::Data {
                kind: DataKind::Scalar,
                val: *_n,
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