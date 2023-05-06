#!/usr/bin/python3
import numpy as np
from gauss_seidel import gauss_seidel
from jacobian import jacobi
print('======= QUESTION 1 ========')
A = np.array([
   [-2, 1, 0.5],
   [1, -2, -0.5],
   [0, 1, 2]
   ])
b = np.array([4, -4, 0])

print('\n>> JACOBI <<')
jacobi(A, b, np.zeros(3), 2)

print('\n>> GAUSS-SEIDAL <<')
gauss_seidel(A, b, np.zeros(3), 2)

print('====== QUESTION 2 =======')
Z = np.array([[4, -1, 0, -1, 0, 0],
              [-1, 4, -1, 0, -1, 0],
              [0, -1, 4, 0 ,0 ,-1],
              [-1 ,0 ,0 ,4 ,-1 ,0],
              [0 ,-1 ,0 ,-1 ,4 ,-1],
              [0 ,0 ,-1 ,0 ,-1 ,4]])
y = np.array([0, 5, 0, 6, -2, 6])

print('\n>> JACOBI <<')
jacobi(Z, y, np.zeros(6), 2)

print('\n>> GUASS-SEDAL <<')
gauss_seidel(Z, y, np.zeros(6), 2)
