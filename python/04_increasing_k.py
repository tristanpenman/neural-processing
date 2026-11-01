#!/usr/bin/env python3

import sys

class MAC_Unit:
    def __init__(self):
        self.accumulator = 0

    def tick(self, a, b):
        # Perform one multiply-accumulate operation
        self.accumulator += a * b

class Matmul_4x4:
    def __init__(self):
        # 2D array of 16 independent MAC units
        self.macs = [
            [MAC_Unit() for j in range(4)]
            for i in range(4)
        ]

    def result(self):
        # Return accumulators as a 4x4 array
        return [
            [self.macs[i][j].accumulator for j in range(4)]
            for i in range(4)
        ]

    def tick(self, A, B, k):
        # These 16 operations are conceptually parallel, since each
        # MAC unit has its own accumulator.
        for i in range(4):
            for j in range(4):
                self.macs[i][j].tick(A[i][k], B[k][j])

# Default value of K
K = 10

# K can also be set from the command line
if len(sys.argv) > 1:
    try:
        K = int(sys.argv[1])
        if K <= 0:
            print('K must be a positive integer.')
            sys.exit(1)
    except:
        print("Could not K as an integer.")
        sys.exit(1)

# Input matrices, first is 4xK
A = [[i * j for i in range(K)] for j in range(4)]

# Second is Kx4
B = [[i + j for i in range(4)] for j in range(K)]

# Initialise a matrix multiplier
matmul = Matmul_4x4()

# Perform K _sequential_ accumulation steps; this would be perform
# one tick per clock cycle on real hardware.
for k in range(K):
    matmul.tick(A, B, k)

# Retrieve the output matrix
C = matmul.result()

# Output the result
for row in C:
    print(row)
