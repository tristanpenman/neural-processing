#!/usr/bin/env python3
"""Multiply matrices using three nested loops."""
# pylint: disable=invalid-name, duplicate-code

import sys

# Default values of M, K and N
M = 8
K = 8
N = 8

# Helper to parse integer arguments
def parse_arg_as_int(argument_index):
    """Parse a positive integer command-line argument."""
    try:
        value = int(sys.argv[argument_index])
        if value <= 0:
            print(f"Argument #{argument_index} must be a positive integer.")
            sys.exit(1)
        else:
            return value
    except ValueError:
        print(f"Could not parse argument #{argument_index} as an integer.")
        sys.exit(1)

# These can also be set from the command line
if len(sys.argv) > 1:
    M = parse_arg_as_int(1)
if len(sys.argv) > 2:
    K = parse_arg_as_int(2)
if len(sys.argv) > 3:
    N = parse_arg_as_int(3)

# Input matrices, first is M x K
A = [[i * j for i in range(K)] for j in range(M)]

# Second is K x N
B = [[i + j for i in range(N)] for j in range(K)]

# Initialize result matrix C with zeros (M x N)
C = [[0 for i in range(N)] for j in range(M)]

# 1. Outer loop: Iterates through each ROW of Matrix A
for i in range(M):
    # 2. Middle loop: Iterates through each COLUMN of Matrix B
    for j in range(N):
        # 3. Inner loop: Accumulate products to calculate dot product
        for k in range(K):
            C[i][j] += A[i][k] * B[k][j]

# Output the result
for row in C:
    print(row)
