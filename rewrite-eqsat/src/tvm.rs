
use std::path::PathBuf;
use egg::RecExpr;

use anyhow::Result;

use crate::TensorLang;

pub type ParserResult = RecExpr<TensorLang>;

#[cfg(not(feature = "tvm"))]
pub fn from_relay(relay_file: PathBuf) -> Result<ParserResult>{
    panic!("To use from_relay compile with llvm support")
}


#[cfg(feature = "tvm")]
use tvm::ir::{IRModule};

#[cfg(feature = "tvm")]
use tvm::ir::relay::{Expr};


#[cfg(feature = "tvm")]
use tvm::runtime::{Error, IsObjectRef};


#[cfg(feature = "tvm")]
pub fn from_relay(relay_file: PathBuf) -> Result<ParserResult>{
    
    let module = match IRModule::parse_file(relay_file)  {
        //Err(ir::module::Error::TVM(Error::DiagnosticError(e))) => return Err(e.into()),
        Err(e) => {
            return Err(e.into());
        }
        Ok(module) => parse_module(module),
    };
    Ok(module)
}

#[cfg(feature = "tvm")]
fn parse_module(module: IRModule) -> ParserResult {
    use egg::{Id, Symbol};
    use tvm::ir::relay::{Call, Constant, Var};
    use tvm::ir::op::Op;


    let main = module.lookup_str("main").unwrap();
    let main_func = main.downcast::<tvm::ir::relay::Function>().unwrap();
    
    println!("Found main function");

    let params = main_func.params.clone();
    let body = main_func.body.clone();

    let mut result = RecExpr::<TensorLang>::default();
    let mut const_counter: usize = 0;

    fn recurse(result: &mut RecExpr<TensorLang>, const_counter: &mut usize, expr : Expr) -> Id{
        
        //Fixme: do we need to clone here?
        if let Ok(call) = expr.clone().downcast::<Call>(){
            
            let mut args_vector = vec![];
            //args_vector.push("extern".parse().unwrap());
            args_vector.push(recurse(result, const_counter, call.op.clone()));
            for arg in call.args.clone() {
                args_vector.push(recurse(result, const_counter, arg));
            }
            
            let call_node = TensorLang::Extern(args_vector.into_boxed_slice());

            
            let call_id = result.add(call_node);
            call_id
        } else if let Ok(op) = expr.clone().downcast::<Op>(){
            let name = op.name.as_str().unwrap();
            //println!("op: {}", name);
            let name_symbol = TensorLang::Symbol(Symbol::from(name));
            let name_id = result.add(name_symbol);
            name_id
        }else if let Ok(constant) = expr.clone().downcast::<Constant>(){
            *const_counter += 1;

            let constant_symbol = TensorLang::Symbol(Symbol::from(format!("const{}", const_counter)));
            let constant_id = result.add(constant_symbol);

            let ndarray = &constant.data;
            let shape = ndarray.shape();
            let shape_ids : Vec<Id> = shape.iter().map(|x|{
                result.add(TensorLang::UInt(*x as usize))
            }).collect();

            let shape_id = result.add(TensorLang::Shape(shape_ids.into_boxed_slice()));

            let constant_tensor = TensorLang::Const([constant_id, shape_id]);
            let constant_id = result.add(constant_tensor);
            constant_id
        }else if let Ok(constant) = expr.clone().downcast::<Var>(){
            let unknown_symbol = TensorLang::Symbol(Symbol::from("var"));
            let unknown_id = result.add(unknown_symbol);
            unknown_id
        } else {
            println!("Unknown: {}", tvm::ir::expr::as_text(expr));
            //let s = expr//.get_type_key();
            //println!("{}", expr.as_ref().get_type_key());
            let unknown_symbol = TensorLang::Symbol(Symbol::from("unknown"));
            let unknown_id = result.add(unknown_symbol);
            unknown_id
        }
    }
    recurse(&mut result, &mut const_counter, body);
    result
    
}