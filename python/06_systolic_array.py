#!/usr/bin/env python3
"""Simulate a square systolic array for matrix multiplication."""
import pprint


class ProcessingElement:
    """Multiply incoming values and forward them to neighboring elements."""

    def __init__(self):
        """Initialize the accumulator and data ports."""
        self.accumulator = 0.0
        self.a_in = 0.0
        self.b_in = 0.0
        self.a_out = 0.0
        self.b_out = 0.0

    def tick(self):
        """Accumulate the current product and prepare values for forwarding."""
        self.accumulator += self.a_in * self.b_in
        self.a_out = self.a_in
        self.b_out = self.b_in

    def reset(self):
        """Clear the accumulator and all input and output ports."""
        self.accumulator = 0.0
        self.a_in = 0.0
        self.b_in = 0.0
        self.a_out = 0.0
        self.b_out = 0.0


class SystolicArray:
    """A square grid of processing elements."""

    def __init__(self, size):
        """Create a grid containing ``size`` rows and columns."""
        self.size = size
        self.grid = [
            [ProcessingElement() for _ in range(size)] for _ in range(size)
        ]

    def tick(self, a_values, b_values):
        """Run one cycle with values injected at the top and left edges."""
        for row_index in range(self.size):
            self.grid[row_index][0].a_in = a_values[row_index]
            self.grid[0][row_index].b_in = b_values[row_index]

        # Snapshot outputs so values move only one cell per cycle.
        a_outputs = [[cell.a_out for cell in row] for row in self.grid]
        b_outputs = [[cell.b_out for cell in row] for row in self.grid]
        for row_index in range(self.size):
            for col_index in range(self.size):
                if col_index > 0:
                    self.grid[row_index][col_index].a_in = a_outputs[row_index][col_index - 1]
                if row_index > 0:
                    self.grid[row_index][col_index].b_in = b_outputs[row_index - 1][col_index]

        for row in self.grid:
            for cell in row:
                cell.tick()

    def result(self):
        """Return accumulated values as a matrix."""
        return [[cell.accumulator for cell in row] for row in self.grid]


def skew_inputs(a_matrix, b_matrix, size):
    """Stagger matrix rows and columns with zeros for systolic execution."""
    total_cycles = 3 * size - 2
    skewed_a = []
    skewed_b = []

    for index in range(size):
        leading_zeros = [0.0] * index
        trailing_zeros = [0.0] * (total_cycles - size - index)
        skewed_a.append(leading_zeros + list(a_matrix[index]) + trailing_zeros)
        column = [b_matrix[row][index] for row in range(size)]
        skewed_b.append(leading_zeros + column + trailing_zeros)

    return skewed_a, skewed_b, total_cycles


def main():
    """Run and print a sample matrix multiplication simulation."""
    size = 4
    a_matrix = [[float(1 + i + j * size) for i in range(size)] for j in range(size)]
    b_matrix = [[float(0.5 + i + j * size) for i in range(size)] for j in range(size)]

    print("A:")
    pprint.pprint(a_matrix)
    print("B:")
    pprint.pprint(b_matrix)

    skewed_a, skewed_b, cycles = skew_inputs(a_matrix, b_matrix, size)
    array = SystolicArray(size)
    for cycle in range(cycles):
        array.tick(
            [skewed_a[row][cycle] for row in range(size)],
            [skewed_b[col][cycle] for col in range(size)],
        )

    print("Result:")
    pprint.pprint(array.result())
    print("Cycles:")
    print(cycles)


if __name__ == "__main__":
    main()
