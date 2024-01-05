#!/usr/bin/env python3
"""Day 11 Advent of Code."""
import numpy as np


def load_input(filename):
    """Return list of maps."""
    map_list = []
    with open(filename) as f:
        lines = []
        for line in f:
            if len(line.rstrip()) == 0:
                map_list.append(np.array(lines, dtype=np.int8))
                lines = []
            else:
                line = [1 if c == '#' else 0 for c in line.rstrip()]
                lines.append(line)
    map_list.append(np.array(lines, dtype=np.int8))

    return map_list

def find_reflection(map_np, num_smudge):
    """Return number of rows/cols above/below reflection axis."""
    rows, cols = map_np.shape
    for i in range(0, rows - 1):
        span = min(i + 1, rows - i - 1)
        top = map_np[i + 1 - span:i + 1, :]
        bot = np.flipud(map_np[i + 1:i + 1 + span, :])
        if (np.equal(top, bot) - 1).sum() == -num_smudge:
            return i + 1, 'horizontal'
        
    for j in range(0, cols - 1):
        span = min(j + 1, cols - j - 1)
        left = map_np[:, j + 1 - span:j + 1]
        right = np.fliplr(map_np[:, j + 1:j + 1 + span])
        if (np.equal(left, right) - 1).sum() == -num_smudge:
            return j + 1, 'vertical'

def main():
    """Load puzzle input and run algorithms."""
    map_list= load_input('input.txt')
    for star in [1, 2]:
        total = 0
        for map_np in map_list:
            num_lines, direction = find_reflection(map_np, star - 1)
            multiplier = 100 if direction == 'horizontal' else 1
            total += multiplier * num_lines
        print(f'Star {star} total = {total}')

if __name__ == "__main__":
    main()
