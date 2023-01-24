use std::path::PathBuf;


#[cfg(feature = "tvm")]
use rewrite_eqsat::tvm::from_relay;



#[cfg(feature = "tvm")]
#[test]
fn test_mobilenet(){
    let mut mobilenet_path = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    mobilenet_path.push("tests/ir/mobilenet.relay");

    if let Ok(mobilenet) = from_relay(mobilenet_path){
        println!("{:?}", mobilenet);
    }else{
        panic!();
    }
}