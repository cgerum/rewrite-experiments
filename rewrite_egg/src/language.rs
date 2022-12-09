#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unconditional_recursion)]

use std::collections::HashSet;
//use std::convert::TryInto;
//use std::time::{Duration, Instant};
use rand;

use egg::*;

define_language! {
    pub enum NNModel {
        "input"     = Input([Id; 1]), // takes a Var, format: name@dim1_dim2...
        "weight"    = Weight([Id; 1]), // takes a Var, format : name@dim1_dim2...
        "ewadd"     = Ewadd([Id; 2]),
        "ewmul"     = Ewmul([Id; 2]),
        "smul"      = Smul([Id; 2]),
        "transpose" = Transpose([Id; 3]), // input, perm_name (format: dim1_dim2...), shuffle
        "matmul"    = Matmul([Id; 3]), // activation, input1, input2
        "conv2d"    = Conv2d([Id; 6]), // conv2d's weight tensor kernel size can not be even, it seems that TASO's output shape computation is incorrect for even kernal size (like 4x4)
        "enlarge"   = Enlarge([Id; 2]), // input_to_enlarge, ref_input
        "dropout"   = Dropout(Id),
        "relu"      = Relu(Id),
        "tanh"      = Tanh(Id),
        "sigmoid"   = Sigmoid(Id),
        "poolmax"   = Poolmax([Id; 7]), // input, kernel_h, kernel_w, stride_h, stride_w, padding, activation
        "poolavg"   = Poolavg([Id; 7]), // input, kernel_h, kernel_w, stride_h, stride_w, padding, activation
        "concat"    = Concat([Id; 4]), // axis, ndim, input1, input2. ndim is for using in CheckApply only
        "concat3"    = Concat3([Id; 5]), // axis, ndim, input1, input2. input3, ndim is for using in CheckApply only
        "concat4"    = Concat4([Id; 6]), // axis, ndim, input1, input2. input3, input4, ndim is for using in CheckApply only
        "concat5"    = Concat5([Id; 7]), // axis, ndim, input1, input2, input3, input4, input5. ndim is for using in CheckApply only
        // Add a concat for each number of inputs if needed
        "split_0"   = Split0(Id), // must take a split node as input
        "split_1"   = Split1(Id), // must take a split node as input
        "split"     = Split([Id; 2]), // axis, input
        "Cpool"     = Cpool([Id; 2]),
        "Iconv"     = Iconv([Id; 2]),
        "Imatmul"   = Imatmul,
        "Iewmul"    = Iewmul,
        "merge"     = Merge([Id; 2]), // merge_gconv, takes [weight, count]
        "reshape"   = Reshape([Id; 2]), // input, shape_name (format: dim1_dim2...)
        "noop"      = Noop([Id; 2]), // No op, use to combine the outputs of a graph in case there are multiple, since egg works with single root graph
        "batchnorm" = BatchNorm([Id; 5]), // input, scale, bias, mean, var
        "complex"   = Complex(Id),
        Num(i32),
        Var(Symbol),
    }
}

#[derive(Debug, PartialEq, Clone, Copy)]
pub enum DataKind {
    Name,
    Scalar,
    Tnsr,
    TnsrTuple,
}

impl Default for DataKind {
    fn default() -> Self {
        DataKind::Name
    }
}

/// Metadata struct for TensorAnalysis
#[derive(Debug, Clone)]
pub struct ValTnsr {
    /// The data type of this eclass, can be a name/scalar/tensor
    pub dtype: DataKind,
    /// The value of this eclass if it is a Scalar type
    pub val: i32,
    /// The name string of this eclass if it is a Name type
    pub name: String,
    /// If the tensor results from all weights computations
    pub all_weights: bool,
}

impl Default for ValTnsr {
    fn default() -> Self {
        ValTnsr {
            ..Default::default()
        }
    }
}


/// Struct for metadata analysis
///
/// In this analysis, it calls functions on the TASO side (e.g. graph.matmul())
/// to create (or get) new ops/nodes and stores pointers to the output tensors.
/// TASO will measure and store the runtime cost when creating a new op/node.
pub struct TensorAnalysis {
    /// Points to the graph object on the TASO side
    //pub graph: std::cell::RefCell<Box<Graph>>,
    /// Record blacklisted nodes for filtering cycles
    pub blacklist_nodes: HashSet<NNModel>,
    /// Newly added nodes by order
    pub newly_added: Vec<NNModel>,
}

impl Default for TensorAnalysis {
    fn default() -> Self {
            // NOTE Box heap-allocates, otherwise any pointer from
            // C++ may be dangling
            TensorAnalysis {
                blacklist_nodes: HashSet::<NNModel>::new(),
                newly_added: Vec::<NNModel>::new(),
            }
    }
}

impl Analysis<NNModel> for TensorAnalysis {
    type Data = ValTnsr;

    /// Merges two metadata when two eclasses are merged.
    fn merge(&mut self, to: &mut Self::Data, from: Self::Data) -> DidMerge {
        if from.all_weights && (!to.all_weights) {
            to.all_weights = from.all_weights;
            DidMerge(true, true)
        } else {
            DidMerge(false,false)
        }
    }

    // Constructs metadata for a new enode, using TASO side functions for tensors.
    fn make(egraph: &EGraph<NNModel, Self>, enode: &NNModel) -> Self::Data {
        let x = |i: &Id| &egraph[*i].data;
        let dim_from_name = |name: &Id| {
            let name_vec: Vec<&str> = x(name).name.split("@").collect();
            assert!(name_vec.len() == 2);
            let dims: Vec<i32> = name_vec[1]
                .split("_")
                .map(|x| x.parse::<i32>().unwrap())
                .collect();
            dims
        };

        match enode {
            NNModel::Matmul([act, a, b]) => {
                // Check types
                assert!(x(act).dtype == DataKind::Scalar);
                assert!(x(a).dtype == DataKind::Tnsr);
                assert!(x(b).dtype == DataKind::Tnsr);

                // Get arguments
                let all_weights = x(a).all_weights && x(b).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::BatchNorm([input, scale, bias, mean, var]) => {
                // Check types
                assert!(x(input).dtype == DataKind::Tnsr);
                assert!(x(scale).dtype == DataKind::Tnsr);
                assert!(x(bias).dtype == DataKind::Tnsr);
                assert!(x(mean).dtype == DataKind::Tnsr);
                assert!(x(var).dtype == DataKind::Tnsr);

                // Get arguments
                let all_weights = x(input).all_weights && x(scale).all_weights && x(bias).all_weights && x(mean).all_weights && x(var).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            },
            NNModel::Conv2d([stride_h, stride_w, pad, act, inpt, wght]) => {
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
                let all_weights = x(inpt).all_weights && x(wght).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Ewadd([a, b]) => {
                // Check types
                assert!(x(a).dtype == DataKind::Tnsr);
                assert!(x(b).dtype == DataKind::Tnsr);

                // Get arguments
                let all_weights = x(a).all_weights && x(b).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Ewmul([a, b]) => {
                // Check types
                assert!(x(a).dtype == DataKind::Tnsr);
                assert!(x(b).dtype == DataKind::Tnsr);

                // Get arguments
                let all_weights = x(a).all_weights && x(b).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Dropout(a) => {
                assert!(x(a).dtype == DataKind::Tnsr);
                let all_weights = x(a).all_weights;

                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }
 
            NNModel::Relu(a) => {
                assert!(x(a).dtype == DataKind::Tnsr);
                let all_weights = x(a).all_weights;

                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(), 
                    all_weights: all_weights,
                }
            }

            NNModel::Tanh(a) => {
                assert!(x(a).dtype == DataKind::Tnsr);
                
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: false,
                }
            }

            NNModel::Sigmoid(a) => {
                assert!(x(a).dtype == DataKind::Tnsr);
                let all_weights = x(a).all_weights;

                
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Input([name]) => {
                // Check types
                assert!(x(name).dtype == DataKind::Name);

                // Get arguments
                let mut dims = dim_from_name(name);
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
                }
            }

            NNModel::Weight([name]) => {
                // Check types
                assert!(x(name).dtype == DataKind::Name);

                // Get arguments
                let mut dims = dim_from_name(name);
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
                }
            }

            NNModel::Concat([axis, ndim, a, b]) => {
                // Check types
                assert!(x(axis).dtype == DataKind::Scalar);
                assert!(x(ndim).dtype == DataKind::Scalar);
                assert!(x(a).dtype == DataKind::Tnsr);
                assert!(x(b).dtype == DataKind::Tnsr);

                // Get arguments
                let axis_val = x(axis).val;
                let all_weights = x(a).all_weights && x(b).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Concat3([axis, ndim, input1, input2, input3]) => {
                // Check types
                assert!(x(axis).dtype == DataKind::Scalar);
                assert!(x(ndim).dtype == DataKind::Scalar);
                assert!(x(input1).dtype == DataKind::Tnsr);
                assert!(x(input2).dtype == DataKind::Tnsr);
                assert!(x(input3).dtype == DataKind::Tnsr);

                // Get arguments
                let axis_val = x(axis).val;
                let all_weights = x(input1).all_weights
                    && x(input2).all_weights
                    && x(input3).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Concat4([axis, ndim, input1, input2, input3, input4]) => {
                // Check types
                assert!(x(axis).dtype == DataKind::Scalar);
                assert!(x(ndim).dtype == DataKind::Scalar);
                assert!(x(input1).dtype == DataKind::Tnsr);
                assert!(x(input2).dtype == DataKind::Tnsr);
                assert!(x(input3).dtype == DataKind::Tnsr);
                assert!(x(input4).dtype == DataKind::Tnsr);

                // Get arguments
                let axis_val = x(axis).val;
                let all_weights = x(input1).all_weights
                    && x(input2).all_weights
                    && x(input3).all_weights
                    && x(input4).all_weights;

                // Create tensorhandle and get metadata
                
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Concat5([axis, ndim, input1, input2, input3, input4, input5]) => {
                // Check types
                assert!(x(axis).dtype == DataKind::Scalar);
                assert!(x(ndim).dtype == DataKind::Scalar);
                assert!(x(input1).dtype == DataKind::Tnsr);
                assert!(x(input2).dtype == DataKind::Tnsr);
                assert!(x(input3).dtype == DataKind::Tnsr);
                assert!(x(input4).dtype == DataKind::Tnsr);
                assert!(x(input5).dtype == DataKind::Tnsr);

                // Get arguments
                let axis_val = x(axis).val;
                let all_weights = x(input1).all_weights
                    && x(input2).all_weights
                    && x(input3).all_weights
                    && x(input4).all_weights
                    && x(input5).all_weights;

                // Create tensorhandle and get metadata
                
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Merge([weight, count]) => {
                // Check types
                assert!(x(count).dtype == DataKind::Scalar);
                assert!(x(weight).dtype == DataKind::Tnsr);

                // Get arguments
                let count_val = x(count).val;
                let all_weights = x(weight).all_weights;

                // Create tensorhandle and get metadat
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Poolmax([inpt, kernel_h, kernel_w, stride_h, stride_w, pad, act]) => {
                // Check types
                assert!(x(kernel_h).dtype == DataKind::Scalar);
                assert!(x(kernel_w).dtype == DataKind::Scalar);
                assert!(x(stride_h).dtype == DataKind::Scalar);
                assert!(x(stride_w).dtype == DataKind::Scalar);
                assert!(x(pad).dtype == DataKind::Scalar);
                assert!(x(act).dtype == DataKind::Scalar);
                assert!(x(inpt).dtype == DataKind::Tnsr);

                // Get arguments
                let kernelH = x(kernel_h).val;
                let kernelW = x(kernel_w).val;
                let strideH = x(stride_h).val;
                let strideW = x(stride_w).val;
                let all_weights = x(inpt).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Poolavg([inpt, kernel_h, kernel_w, stride_h, stride_w, pad, act]) => {
                // Check types
                assert!(x(kernel_h).dtype == DataKind::Scalar);
                assert!(x(kernel_w).dtype == DataKind::Scalar);
                assert!(x(stride_h).dtype == DataKind::Scalar);
                assert!(x(stride_w).dtype == DataKind::Scalar);
                assert!(x(pad).dtype == DataKind::Scalar);
                assert!(x(act).dtype == DataKind::Scalar);
                assert!(x(inpt).dtype == DataKind::Tnsr);

                // Get arguments

                let kernelH = x(kernel_h).val;
                let kernelW = x(kernel_w).val;
                let strideH = x(stride_h).val;
                let strideW = x(stride_w).val;
                let all_weights = x(inpt).all_weights;

                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Split([axis, inpt]) => {
                // Check types
                assert!(x(axis).dtype == DataKind::Scalar);
                assert!(x(inpt).dtype == DataKind::Tnsr);

                // Get arguments

                let axis_val = x(axis).val;
                let all_weights = x(inpt).all_weights;

                // Create tensorhandle and get metadata
                
                    Self::Data {
                        dtype: DataKind::TnsrTuple,
                        val: 0,
                        name: String::new(),
                        all_weights: all_weights,
                    }
                
            }

            NNModel::Split0(inpt) => {
                // Check types
                assert!(x(inpt).dtype == DataKind::TnsrTuple);
                let all_weights = x(inpt).all_weights;


                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Split1(inpt) => {
                // Check types
                assert!(x(inpt).dtype == DataKind::TnsrTuple);
                let all_weights = x(inpt).all_weights;

                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Enlarge([a, b]) => {
                // Check types
                assert!(x(a).dtype == DataKind::Tnsr);
                assert!(x(b).dtype == DataKind::Tnsr);

                // Get arguments
                let all_weights = x(a).all_weights && x(b).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Reshape([inpt, shape_name]) => {
                // Check types
                assert!(x(shape_name).dtype == DataKind::Name);
                assert!(x(inpt).dtype == DataKind::Tnsr);

                // Get arguments
                let dims: Vec<i32> = x(shape_name)
                    .name
                    .split("_")
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect();
                let all_weights = x(inpt).all_weights;

                // Create tensorhandle and get metadata
                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Transpose([inpt, perm_name, shuffle]) => {
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
                }
            }

            NNModel::Noop([a, b]) => {
                // Check types
                assert!(x(a).dtype == DataKind::Tnsr);
                assert!(x(b).dtype == DataKind::Tnsr);
                let all_weights = x(a).all_weights && x(b).all_weights;

                Self::Data {
                    dtype: DataKind::Tnsr,
                    val: 0,
                    name: String::new(),
                    all_weights: all_weights,
                }
            }

            NNModel::Num(_n) => Self::Data {
                dtype: DataKind::Scalar,
                val: *_n,
                name: String::new(),
                all_weights: false,
            },

            NNModel::Var(_s) => Self::Data {
                dtype: DataKind::Name,
                val: 0,
                name: _s.as_str().to_string(),
                all_weights: false,
            },

            other => {
                println!("{:?}", other);
                todo!()
            }
        }
    }

    // Not needed to modify anything
    fn modify(egraph: &mut EGraph<NNModel, Self>, id: Id) {}
}

