
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
    use tvm::ir::relay::Call;


    let main = module.lookup_str("main").unwrap();
    let main_func = main.downcast::<tvm::ir::relay::Function>().unwrap();
    
    println!("Found main function");

    let params = main_func.params.clone();
    let body = main_func.body.clone();
    let recurse = |expr : &Expr| {
        
        if let Ok(call) = expr.downcast::<Call>() {
            
        }else{
            println!("Unhandled expression {:?}", expr);
        }
    };
    recurse(&body);
    "nil".parse().unwrap()
    
}