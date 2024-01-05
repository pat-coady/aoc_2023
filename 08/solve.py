#!/usr/bin/env python3
"""Day 08 Advent of Code."""
import functools
import re
from collections import Counter


def load_input(filename):
    """Return list of 2-tuples with (hand, bid)."""
    with open(filename) as f:
        turns = f.readline().rstrip()
        f.readline()
        graph = {}
        for line in f:
            node, left, right = re.findall(r'\w+', line)
            graph[node] = (left, right)
    
    return turns, graph

def factors(m):
    """Return Counter of prime factors of m."""
    factor_counts = Counter()
    i = 2
    while i <= int(m ** 0.5):
        if m % i == 0:
            factor_counts[i] += 1
            m = m // i
        else:
            i += 1
    factor_counts[m] += 1

    return factor_counts


def common_factors(f_count1, f_count2):
    """Return Counter with least common factors of f_count1 and f_count2."""
    factors = Counter()
    for f in set(list(f_count1.keys()) + list(f_count2.keys())):
        factors[f] = max(f_count1[f], f_count2[f])
    
    return factors


def main():
    """Load input and call algorithms."""
    instructions, graph = load_input('input.txt')
    instructions = [0 if x == 'L' else 1 for x in instructions]
    for star in [1, 2]:
        nodes = [i for i in graph if i[2] == 'A'] if star == 2 else ['AAA']
        z_idxs = []
        i = 0
        while True:
            inst = instructions[i % len(instructions)]
            i += 1
            nodes = [graph[node][inst] for node in nodes]
            if len([i for i in nodes if i[2] == 'Z']) > 0:
                z_idxs.append(i)
            if len(z_idxs) == len(nodes):
                break
        z_factors = [factors(x) for x in z_idxs]
        cfs = functools.reduce(common_factors, z_factors)
        product = functools.reduce(lambda x, y: x * y, list(cfs.values()) + list(cfs.keys()))
        print(f'Star {star} steps = {product}')


if __name__ == "__main__":
    main()
