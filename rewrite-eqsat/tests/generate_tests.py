import os
from tvm.relay.testing import mobilenet, resnet
from tvm.relay.transform import SimplifyInference, FoldScaleAxis, FoldConstant
from tvm.ir.transform import Sequential
from tvm.relay.build_module import bind_params_by_name
from tvm import relay

def get_simple_net(batch_size = 1, out_channels = 16):

    data = relay.var("data", relay.TensorType((batch_size, 3, 224, 224), "float32"))
    weight = relay.var("weight")

    simple_net = relay.nn.conv2d(
        data=data, weight=weight, kernel_size=(3, 3), channels=out_channels, padding=(1, 1)
    )
    simple_net = relay.nn.relu(simple_net)
    simple_net = relay.Function(relay.analysis.free_vars(simple_net), simple_net)

    net, params = relay.testing.create_workload(simple_net)
    
    return net, params

workloads = [
    ("mobilenet", mobilenet.get_workload, {}),
    ("resnet18", resnet.get_workload, {'num_layers': 18}),
    ("simple_net", get_simple_net, {}),
]


for name, get_workload, args in workloads:
    mod, params = get_workload(**args)

    os.makedirs("ir", exist_ok=True)


    transforms = Sequential([SimplifyInference(), FoldScaleAxis(), FoldConstant()])
    mod["main"] = bind_params_by_name(mod["main"], params)

    mod = transforms(mod)

    text =  mod.astext()

    with open(f"ir/{name}.relay", "w") as f:
        f.write(text)
