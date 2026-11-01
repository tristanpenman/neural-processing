#!/usr/bin/env python3

import sys

# Default values of M, K and N
M = 8
K = 8
N = 8

# Helper to parse integer arguments
def parse_int(i):
    try:
        value = int(sys.argv[i])
        if value <= 0:
            print(f"Argument #{i} must be a positive integer.")
            sys.exit(1)
        else:
            return value
    except:
        print(f"Could not parse argument #{i} as an integer.")
        sys.exit(1)

# These can also be set from the command line
if len(sys.argv) > 1:
    M = parse_int(1)
if len(sys.argv) > 2:
    K = parse_int(2)
if len(sys.argv) > 3:
    N = parse_int(3)

# Input matrices, first is M x K
A = [[i * j for i in range(K)] for j in range(M)]

# Second is K x N
B = [[i + j for i in range(N)] for j in range(K)]

# Initialize result matrix C with zeros (M x N)
C = [[0 for i in range(N)] for j in range(M)]

# A simple Multiply-Accumulate class that knows how to
# calculate a product and add it to an accumulator.
class MAC_Unit:
    def __init__(self):
        self.accumulator = 0

    def tick(self, a, b):
        # Perform one multiply-accumulate operation
        self.accumulator += a * b

# Rows of A
for i in range(M):
    # Columns of B
    for j in range(N):
        # Create a fresh accumulator
        mac = MAC_Unit()

        # Calculate dot product
        for k in range(K):
            a = A[i][k]
            b = B[k][j]
            mac.tick(a, b)

        # Save the value of the accumulator
        C[i][j] = mac.accumulator

# Output the result
for row in C:
    print(row)
