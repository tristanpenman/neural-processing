#!/usr/bin/env python3
"""Multiply matrices using a dedicated multiply-accumulate unit."""

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

# A simple Multiply-Accumulate class that knows how to
# calculate a product and add it to an accumulator.
class MAC_Unit:
    """Accumulate products of input values."""

    def __init__(self):
        """Initialize the accumulator to zero."""
        self.accumulator = 0

    def tick(self, left_value, right_value):
        """Multiply inputs and add their product to the accumulator."""
        # Perform one multiply-accumulate operation
        self.accumulator += left_value * right_value

    def reset(self):
        """Clear the accumulated value."""
        self.accumulator = 0

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
