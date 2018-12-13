#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

# create vector or matrix
vector = np.array([1,2,3])
print(vector)
matrix = np.array([(1,2,3), (1,2,3)])
print(matrix)

matrix_1 = np.arange(6).reshape(2,3)

# simple operator

print(vector * 2)

print(matrix * 2)

# matrix operator
## elementwise product
print(matrix * matrix_1)
## matrix product
## tutorial says ok, but under my env not ok
# print(matrix @ matrix_1) 

## another matrix product
print(matrix.dot(matrix_1.reshape(3,2)))

