#!/usr/bin/env python3
"""Day 11 Advent of Code."""
import re


def load_input(filename):
    """Return list of springs and contiguous groupings."""
    spring_list = []
    with open(filename) as f:
        for line in f:
            springs, groups = line.rstrip().split(' ')
            groups = [int(x) for x in groups.split(',')]
            spring_list.append([springs, groups])
    return spring_list

def greedy_match(springs, groups, memo):
    """Recursively match groups to springs with memoization."""
    memo_key = springs + str(groups)
    if memo_key in memo:
        return memo[memo_key]
    if len(groups) == 0:
        return 1 if '#' not in springs else 0 
    springs = springs.lstrip('.')
    if len(springs) == 0:
        return 0
    num_springs = groups[0]
    pattern = '[?#]' * num_springs + '[\.?]'
    m = re.match(pattern, springs)
    if m is None:
        total = 0
    else:
        new_groups = groups[1:]
        start, end = m.span()
        total = greedy_match(springs[end:], new_groups, memo)
    if springs[0] == '?':
        total += greedy_match(springs[1:], groups, memo)

    memo[memo_key] = total
    return total

def main():
    """Load puzzle input and run algorithms."""
    spring_list = load_input('input.txt')
    for star in [1, 2]:
        total = 0
        for springs, groups in spring_list:
            if star == 2:
                springs = ((springs + '?') * 5)[:-1]
                groups = groups * 5
            total += greedy_match(springs + '.', groups, {})
        print(f'Star {star} total = {total}')


if __name__ == "__main__":
    main()
