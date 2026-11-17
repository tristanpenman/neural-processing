# Neural Processing

Python examples that illustrate concepts in matrix multiplication, NPU and TPU architecture, and tensor operations.

This is intended as complementary material for my post _[Neural Processing from the Gound Up](https://tristanpenman.com/blog/posts/2026/11/17/neural-processing-from-the-ground-up)_, which introduces the concepts that underlie neural processing, and explores how different neural network accelerators realise those concepts in silicon.

## Dependencies

These examples have minimal dependencies, and should run directly using your system Python.

Alternatively, start a Python 3.11 shell using Docker Compose:

```
./scripts/python-shell.sh
```

## Tests

A small test suite has been included:

```
./python/test.sh
```

This uses results from example 1 ([01_nested_loops.py](python/01_nested_loops.py)) as ground truth when running example 2 onwards.

## Examples

Basic examples working up to tiling:

- [01_nested_loops.py](python/01_nested_loops.py) - Naive matrix multiplication using nested loops.
- [02_mac_unit.py](python/02_mac_unit.py) - Refactor first example to use a Multiply-Accumulate (MAC) unit.
- [03_matmul_4x4.py](python/03_matmul_4x4.py) - Introduce a specialised 4x4 matrix multiplier.
- [04_increasing_k.py](python/04_increasing_k.py) - Shows that we can arbitrarily scale the shared dimension K.
- [05_tiling.py](python/05_tiling.py) - Handle arbitrary matrices using a 4x4 matrix multiplier.

Advanced examples illustrating systolic array architectures:

- [06_systolic_array.py](./06_systolic_array.py) - Simulate a systolic array for matrix multiplication.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
