#!/bin/sh
set -eu

cd "$(dirname "$0")"
python=${PYTHON:-python3}
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT HUP INT TERM

check() {
    label=$1
    shift
    "$@" > "$tmpdir/actual"
    if ! cmp -s "$tmpdir/expected" "$tmpdir/actual"; then
        printf 'FAIL: %s output differs from 01_nested_loops.py\n' "$label" >&2
        diff -u "$tmpdir/expected" "$tmpdir/actual" >&2 || true
        exit 1
    fi
    printf 'PASS: %s\n' "$label"
}

# Same dimensions for the general MAC implementation.
"$python" 01_nested_loops.py 5 7 6 > "$tmpdir/expected"
check '02_mac_unit.py (5x7x6)' "$python" 02_mac_unit.py 5 7 6

# The specialized multiplier is fixed at 4x4.
"$python" 01_nested_loops.py 4 4 4 > "$tmpdir/expected"
check '03_matmul_4x4.py' "$python" 03_matmul_4x4.py

# This example varies K while keeping M and N at 4.
"$python" 01_nested_loops.py 4 7 4 > "$tmpdir/expected"
check '04_increasing_k.py (K=7)' "$python" 04_increasing_k.py 7

# Exercise partial tiles in both dimensions as well as a full shared dimension.
"$python" 01_nested_loops.py 5 7 6 > "$tmpdir/expected"
check '05_tiling.py (5x7x6)' "$python" 05_tiling.py 5 7 6

printf 'All checks passed.\n'
