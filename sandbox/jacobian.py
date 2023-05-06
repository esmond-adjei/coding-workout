#!/usr/bin/python3
import numpy as np

def jacobi(A, b, x0, its):
  # Get the diagonal matrix D and the remainder matrix R
  D = np.diag(np.diag(A))
  R = A - D

  # Initialize x and error
  x = x0
  err = np.linalg.norm(A @ x - b)

  # Iterate until error is below tolerance
  while its:
    # Update x using Jacobi formula
    x = np.linalg.inv(D) @ (b - (R @ x))
    print(x)
    # Calculate error
    err = np.linalg.norm(A @ x - b)
    its -= 1
  return x

