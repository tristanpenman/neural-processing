# Neural Processing

Python examples that illustrate concepts in matrix multiplication, NPU and TPU architecture, and tensor operations.

## Dependencies

These examples have minimal dependencies, so it should be possible to run them directly using your system Python.

Alternatively, use [`python-shell.sh`](scripts/python-shell.sh) to start a Python 3 shell in Docker. The container installs dependencies from [requirements.txt](python/requirements.txt).

## Examples

- [01_nested_loops.py](python/01_nested_loops.py) - Naive matrix multiplication using nested loops.
- [02_mac_unit.py](python/02_mac_unit.py) - Refactor first example to use a Multiply-Accumulate (MAC) unit.
- [03_matmul_4x4.py](python/03_matmul_4x4.py) - Introduce a specialised 4x4 matrix multiplier.
- [04_increasing_k.py](python/04_increasing_k.py) - Shows that we can arbitrarily scale the shared dimension K.
- [05_tiling.py](python/05_tiling.py) - Handle arbitrary matrices using a 4x4 matrix multiplier.
