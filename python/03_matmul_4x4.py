#!/usr/bin/env python3
"""Multiply two 4x4 matrices with independent MAC units."""

class MAC_Unit:
    """Accumulate products of input values."""

    def __init__(self):
        """Initialize the accumulator to zero."""
        self.accumulator = 0

    def tick(self, a, b):
        """Multiply inputs and add their product to the accumulator."""
        # Perform one multiply-accumulate operation
        self.accumulator += a * b

    def reset(self):
        """Clear the accumulated value."""
        self.accumulator = 0

class Matmul_4x4:
    """Model a fixed 4x4 array of multiply-accumulate units."""

    def __init__(self):
        """Initialize the 4x4 array."""
        # 2D array of 16 independent MAC units
        self.macs = [
            [MAC_Unit() for j in range(4)]
            for i in range(4)
        ]

    def result(self):
        """Return the current accumulators as a 4x4 matrix."""
        # Return accumulators as a 4x4 array
        return [
            [self.macs[i][j].accumulator for j in range(4)]
            for i in range(4)
        ]

    def tick(self, a_matrix, b_matrix, shared_index):
        """Accumulate products for a shared-dimension index."""
        # These 16 operations are conceptually parallel, since each
        # MAC unit has its own accumulator.
        for i in range(4):
            for j in range(4):
                self.macs[i][j].tick(a_matrix[i][shared_index], b_matrix[shared_index][j])

# Input matrices, both 4x4
A = [[i * j for i in range(4)] for j in range(4)]
B = [[i + j for i in range(4)] for j in range(4)]

# Initialise a matrix multiplier
matmul = Matmul_4x4()

# Perform four _sequential_ accumulation steps; this would be perform
# one tick per clock cycle on real hardware.
for k in range(4):
    matmul.tick(A, B, k)

# Retrieve the output matrix
C = matmul.result()

# Output the result
for row in C:
    print(row)
