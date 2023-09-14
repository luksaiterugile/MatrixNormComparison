# MatrixNormComparison
## Norms of Matrices and Pseudo-Inverse Matrices

This repository contains Python code to generate random 3x6 matrices, calculate their norms, compute their pseudo-inverses, and compare the norms of both matrices. The goal is to explore any regularity or additivity between the norms of these matrices.

## Overview
This program investigates the relationship between the norms of randomly generated 3x6 matrices and the norms of their corresponding pseudo-inverse matrices. We perform the following steps for 10,000 iterations:
1. Generate a random 3x6 matrix with elements in the interval [-1, 1].
2. Calculate the norm of the random matrix.
3. Compute the pseudo-inverse of the random matrix.
4. Calculate the norm of the pseudo-inverse matrix.

The norms of both matrices are plotted as histograms using Matplotlib to visualize any regularities or additivity.

## Requirements
To run this code, you need the following Python libraries installed: 
- NumPy
- Matplotlib

## Program usage
Command to run the Python script:
```
python matrix_norm_comparison.py
```
The script will generate the histograms and save the results as an image file (matrix_comparison_histogram.png) in the same directory.
