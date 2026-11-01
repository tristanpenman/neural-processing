#!/usr/bin/env python3

# Matrix A (2x3)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matrix B (3x2)
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Initialize Result Matrix C with zeros (2x2)
# Dimensions of C match rows of A and columns of B
C = [[0, 0],
     [0, 0]]

# 1. Outer loop: Iterates through each ROW of Matrix A
for i in range(len(A)):
    # 2. Middle loop: Iterates through each COLUMN of Matrix B
    for j in range(len(B[0])):
        # 3. Inner loop: Accumulate products to calculate dot product
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# Output the result
for row in C:
    print(row)
