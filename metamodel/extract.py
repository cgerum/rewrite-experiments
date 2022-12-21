import inspect

def build_torch_model():
    import torch.nn.functional as f
    for name, func in inspect.getmembers(f, inspect.isfunction):
        print(name, end=":\n")
        signature = inspect.signature(func)
        print(signature)
        desc = inspect.getdoc(func)
        print()
    
    
if __name__ == "__main__":
    build_torch_model()