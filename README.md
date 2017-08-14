Simple test to check out the overhead differences in calling a pure C function and a Go function exposed as a C function from python.

Motivation:

Go is an up-and-coming language with several attractive features including first-class concurrency support via go-routines, cross-compilation build tools and easy to read syntax. Since Go can be compiled into C callable libraries, it can also be called from Python. However, just because you can, doesn't mean you should. The ability to call goroutines from python is rather tempting way to deal with python's awkward multiprocessing library. However, calling a Go library will spawn the go runtime and all that it entails (threads, garbage collector etc). This introduces some overhead that would not otherwise be present if calling an equivalent library written purely in C.

Goal:

1. Determine the scale of the overhead when calling Go libraries in comparison to C libraries.

Method:

1. Create identical simple functions in both Go and C in which the function call overhead is signification compared to the function implementation (ie return a constant, add two integers etc.)

2. Call these function N  times from python and compare how long each takes.

