#!/usr/bin/python3
import numpy as np

def gauss_seidel(A, b, x0, its=1):
    x = x0
    while its:
        # Loop over each equation
        for i in range(len(b)):
            # Calculate the sum of Ax except x[i]
            s = np.dot(A[i,:], x) - A[i,i] * x[i]
            # Update x[i] using Gauss-Seidel formula
            x[i] = (b[i] - s) / A[i,i]
        print(x)
        # Calculate the error as the norm of Ax-b
        err = np.linalg.norm(np.dot(A,x) - b)
        # Increment the iteration counter
        its -= 1

    return x

