#!/usr/bin/env python3
"""Day 14 Advent of Code."""
import numpy as np
from scipy.signal import convolve2d


def load_input(filename):
    """Return map of round (1) and cube (3) rocks."""
    with open(filename) as f:
        lines = [['.O_#'.find(c) for c in line.rstrip()] for line in f]
    return np.array(lines, dtype=np.int8)

def roll_rocks(map_np):
    """Roll all round rocks to the North."""
    rows, cols = map_np.shape
    filter = np.array([[-1], [1]], dtype=np.int8)
    for _ in range(rows):
        roll = convolve2d(map_np, filter, 'valid')
        round_rocks = roll == -1
        add_rocks = np.pad(round_rocks, ((0, 1), (0, 0)), 'constant', constant_values='0')
        remove_rocks = np.pad(round_rocks, ((1, 0), (0, 0)), 'constant', constant_values='0')
        map_np += add_rocks * 1 - remove_rocks * 1

    return map_np

def spin_cycle(map_np):
    """Roll all round rocks in direction."""
    rows, cols = map_np.shape
    filter_pads = [
        ([[-1], [1]], ((0, 1), (0, 0)), ((1, 0), (0, 0))),
        ([[-1, 1]], ((0, 0), (0, 1)), ((0, 0), (1, 0))),
        ([[1], [-1]], ((1, 0), (0, 0)), ((0, 1), (0, 0))),
        ([[1, -1]], ((0, 0), (1, 0)), ((0, 0), (0, 1))),
        ]
    cycle_count = {}
    i = 0
    while True:
        i += 1
        for filter, pad1, pad2 in filter_pads:
            filter = np.array(filter, dtype=np.int8)
            for _ in range(rows):
                roll = convolve2d(map_np, filter, 'valid')
                round_rocks = roll == -1
                add_rocks = np.pad(round_rocks, pad1, 'constant', constant_values='0')
                remove_rocks = np.pad(round_rocks, pad2, 'constant', constant_values='0')
                map_np += add_rocks * 1 - remove_rocks * 1
        key = hash(map_np.data.tobytes())
        if key in cycle_count:
            cycle_len = i - cycle_count[key]
            if (1000000000 - cycle_count[key]) % cycle_len == 0:
                break
        else:
            cycle_count[key] = i
            
    return map_np

def total_load(map_np):
    """Return total load of round rocks."""
    rows, cols = map_np.shape
    weights = np.arange(rows, 0, -1, dtype=np.int8)

    return ((map_np == 1).sum(axis=1) * weights).sum()

def main():
    """Load puzzle input and run algorithms."""
    map_np = load_input('input.txt')
    map_np = roll_rocks(map_np)
    print(f'Star 1 load = {total_load(map_np)}')
    map_np = load_input('input.txt')
    map_np = spin_cycle(map_np)
    print(f'Star 2 load = {total_load(map_np)}')

if __name__ == "__main__":
    main()
