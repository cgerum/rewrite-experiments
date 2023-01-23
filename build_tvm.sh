#!/bin/bash


mkdir -p external/tvm/build
pushd external/tvm/build
cmake -G Ninja .. 
ninja
popd