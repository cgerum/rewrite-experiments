import os
from tvm.relay.testing import mobilenet
from tvm.relay.transform import SimplifyInference, FoldScaleAxis, FoldConstant
from tvm.ir.transform import Sequential
from tvm.relay.build_module import bind_params_by_name

mod, params = mobilenet.get_workload()

os.makedirs("ir", exist_ok=True)


transforms = Sequential([SimplifyInference(), FoldScaleAxis(), FoldConstant()])
mod["main"] = bind_params_by_name(mod["main"], params)

mod = transforms(mod)

text =  mod.astext()

with open("ir/mobilenet.relay", "w") as f:
    f.write(text)
