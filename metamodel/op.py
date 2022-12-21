from typing import Any, Mapping, TypeVar, NamedTuple, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class Op:
    name: str
    arguments: Mapping[str, Any]
    attrs: Mapping[str, Any]
    desc: Optional[str] = None
    
    
    
if __name__ == "__main__":
    conv_op = Op("conv", {}, {})
    
    print(conv_op)
    
