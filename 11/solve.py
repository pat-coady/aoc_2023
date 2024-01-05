#!/usr/bin/env python3
"""Day 11 Advent of Code."""
import numpy as np


def load_input(filename):
    """Return map of galaxies."""
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append([0 if c == '.' else 1 for c in line.rstrip()])

    return np.array(lines, dtype=np.int8)

def galaxy_list(universe):
    """Return list of galaxy locations (pre-expansion) and empty row and col locations."""
    g_array = np.argwhere(universe == 1)
    empty_row_array = np.argwhere(universe.sum(axis=1) == 0).flatten()
    empty_col_array = np.argwhere(universe.sum(axis=0) == 0).flatten()

    return g_array, empty_col_array, empty_row_array

def all_pair_dist(g_array, col_array, row_array, exp_factor):
    """Return all pair shortest distance given list of galaxy locs and empty rows/cols."""
    total = 0
    for loc1 in g_array:
        for loc2 in g_array:
            total += np.abs(loc1 - loc2).sum()
            total += ((exp_factor - 1) *
                      ((col_array < max(loc1[1], loc2[1])) *
                       (col_array > min(loc1[1], loc2[1]))).sum())
            total += ((exp_factor - 1) *
                      ((row_array < max(loc1[0], loc2[0])) *
                       (row_array > min(loc1[0], loc2[0]))).sum())

    return total // 2

def main():
    """Load input and call algorithms."""
    universe = load_input('input.txt')
    g_array, e_col_array, e_row_array = galaxy_list(universe)
    for star, exp_factor in [(1, 2), (2, 1000000)]:
        dist = all_pair_dist(g_array, e_col_array, e_row_array, exp_factor)
        print(f'Star {star} total distance = {dist}')

if __name__ == "__main__":
    main()
