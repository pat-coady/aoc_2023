#!/usr/bin/env python3
"""Day 09 Advent of Code."""
import numpy as np


def load_input(filename):
    """Return list sequences (np.int arrays)."""
    seqs = []
    with open(filename) as f:
        for line in f:
            seqs.append(np.array([int(x) for x in line.rstrip().split(' ')], dtype=np.int32))

    return seqs

def next_val(seq):
    """Return next value in sequence by recursing np.diff function until all 0s."""
    return 0 if seq.sum() == 0 else seq[-1] + next_val(np.diff(seq))

def main():
    """Load input and call algorithms."""
    seqs = load_input('input.txt')
    for star in [1, 2]:
        next_vals = np.array([next_val(seq) for seq in seqs])
        print(f'Star {star} next value sum = {next_vals.sum()}')
        seqs = [np.flip(seq) for seq in seqs]

if __name__ == "__main__":
    main()
