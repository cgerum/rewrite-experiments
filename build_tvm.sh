#!/bin/bash -e

source ./env

mkdir -p $TVM_HOME/build
pushd $TVM_HOME/build
cmake -G Ninja .. 
ninja
popd