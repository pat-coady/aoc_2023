#!/usr/bin/env python3
"""Day 03 Advent of Code."""
import functools
import re

import numpy as np

CONNECTED_TO_SYMBOL = [(-1, -1), (-1, 0), (-1, 1),
         (0, -1), (0, 1),
         (1, -1), (1, 0), (1, 1),
         ]

CONNECTED_TO_DIGIT = [(0, -1), (0, 1)]

def issymbol(c):
    """Return True if character is not a `.` and not a digit."""
    return not c.isdigit() and c != '.'


def input_to_numpy(filename, asterisk_only=False):
    """Load text input and return numpy digit map and symbol map."""
    digits, symbols = [], []
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            digits.append([int(c) if c.isdigit() else -1 for c in line])
            if asterisk_only:
                symbols.append([1 if c == '*' else 0 for c in line])
            else:
                symbols.append([1 if issymbol(c) else 0 for c in line])

    return np.array(digits, dtype=np.int8), np.array(symbols, dtype=np.int8)


def flood(start, digits, connected_digits, visited, moves):
    """Recursive flood fill of occupied digit locations."""
    if visited[start] == 1:
        return
    visited[start] = 1
    i, j = start
    for move in moves:
        next_loc = (i + move[0], j + move[1])
        if digits[next_loc] > -1:
            connected_digits[next_loc] = 1
            flood(next_loc, digits, connected_digits, visited,
                  CONNECTED_TO_DIGIT)


def flood_fill(digits, symbols):
    """Return binary (1, 0) numpy array with digit locations connected to a symbol."""
    digits = np.pad(digits, 1, mode='constant', constant_values=-1)
    symbols = np.pad(symbols, 1, mode='constant', constant_values=0)
    connected_digits = np.zeros_like(digits, dtype=np.int8)
    visited = np.zeros_like(connected_digits)
    m, n = digits.shape
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if symbols[i, j] == 1:
                flood((i, j), digits, connected_digits, visited,
                      CONNECTED_TO_SYMBOL)

    return connected_digits


def get_nums(digits, connected_digits):
    """Turn connected digits into list of numbers."""
    rows, cols = digits.shape
    connected_digits = connected_digits[1:-1, 1:-1]  # remove padding
    digit_list = []
    for i in range(rows):
        for j in range(cols):
            if connected_digits[i, j] == 1:
                digit_list.append(str(digits[i, j]))
            else:
                digit_list.append('.')
        digit_list.append('.')  # digits cannot wrap across rows
    digit_str = ''.join(digit_list)
    num_list = re.findall(r'\d+', digit_str)
    
    return [int(x) for x in num_list]
    

def star1(filename):
    """Star 1 algorithm."""
    digits, symbols = input_to_numpy(filename)
    connected_digits = flood_fill(digits, symbols)
    num_list = get_nums(digits, connected_digits)
    
    return functools.reduce(lambda x, y: x + y, num_list)


def gear_ratios(digits, symbols):
    """Return binary (1, 0) numpy array with digit locations connected to a symbol."""
    ratio_list = []
    digits = np.pad(digits, 1, mode='constant', constant_values=-1)
    symbols = np.pad(symbols, 1, mode='constant', constant_values=0)
    visited = np.zeros_like(digits)
    m, n = digits.shape
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            connected_digits = np.zeros_like(digits, dtype=np.int8)
            if symbols[i, j] == 1:
                flood((i, j), digits, connected_digits, visited,
                      CONNECTED_TO_SYMBOL)
                gears = get_nums(digits[1:-1, 1:-1], connected_digits)
                if len(gears) == 2:
                    ratio_list.append(gears[0] * gears[1])
    
    return functools.reduce(lambda x, y: x + y, ratio_list)


def star2(filename):
    """Star 2 algorithm."""
    digits, symbols = input_to_numpy(filename, asterisk_only=True)
    
    return gear_ratios(digits, symbols)


def main():
    """Call star solutions."""
    filename = 'input.txt'
    print(f'Star 1 total = {star1(filename)}')
    print(f'Star 2 total = {star2(filename)}')


if __name__ == "__main__":
    main()
