## A Simple Example of Extending Python with C or C++

### 1 step: define C/C++ files
- prepare C function(s) of the module
- define `PyMethodDef` list including the functions
- define `PyModuleDef` struct with PyMethodDef list
- write `PyInit_$MODULE_NAME` func to create module

### 2 step: build
- the `setup.py` file
- build & install

### 3 test
just import and try

see more [@docs.python.org](https://docs.python.org/3/extending/index.html)

