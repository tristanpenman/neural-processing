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

    def tick(self, A, B, k, row_offset, col_offset, max_m, max_n):
        # These 16 operations are conceptually parallel, since each
        # MAC unit has its own accumulator.
        for i in range(4):
            # Ensure current row is in range
            if row_offset + i >= max_m:
                break
            for j in range(4):
                # Ensure current column is in range
                if col_offset + j >= max_n:
                    break
                self.macs[i][j].tick(A[i + row_offset][k], B[k][j + col_offset])

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
    except ValueError:
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

# Output matrix, M x N
C = [[0 for i in range(N)] for j in range(M)]

# Tiles are each 4 x 4 in size
for row_offset in range(0, M, 4):
    for col_offset in range(0, N, 4):
        # Initialise a matrix multiplier for this tile
        matmul = Matmul_4x4()

        # Perform K _sequential_ accumulation steps; this would be perform
        # one tick per clock cycle on real hardware.
        for k in range(K):
            matmul.tick(A, B, k, row_offset, col_offset, M, N)

        # Copy the valid part of tile.result() into C at [row_offset:, col_offset:]
        tile_result = matmul.result()
        for row_index in range(min(4, M - row_offset)):
            for col_index in range(min(4, N - col_offset)):
                C[row_offset + row_index][col_offset + col_index] = tile_result[row_index][col_index]

# Output the result
for row in C:
    print(row)
