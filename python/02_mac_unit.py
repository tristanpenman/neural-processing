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
# Dimensions of C match rows of A and columns of B.
C = [[0, 0],
     [0, 0]]

# A simple Multiply-Accumulate class that knows how to
# calculate a product and add it to an accumulator.
class MAC_Unit:
    def __init__(self):
        self.accumulator = 0

    def tick(self, a, b):
        # Perform one multiply-accumulate operation
        self.accumulator += a * b

# Rows of A
for i in range(len(A)):
    # Columns of B
    for j in range(len(B[0])):
        # Create a fresh accumulator
        mac = MAC_Unit()

        # Calculate dot product
        for k in range(len(B)):
            a = A[i][k]
            b = B[k][j]
            mac.tick(a, b)

        # Save the value of the accumulator
        C[i][j] = mac.accumulator

# Output the result
for row in C:
    print(row)
