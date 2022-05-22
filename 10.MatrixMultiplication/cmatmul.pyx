from libcpp.vector cimport vector

cdef extern from "matmul.hpp":
    ctypedef vector[vector[int]] matrix
    matrix multiplyChain(vector[matrix] chain)

def multiply_chain(chain):
    return multiplyChain(chain)
