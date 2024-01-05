#!/usr/bin/env python3
"""Day 10 Advent of Code."""
import numpy as np


def load_input(filename):
    """Return list sequences (np.int arrays)."""
    with open(filename) as f:
        pipes = [line.rstrip() for line in f]
    
    return pipes

def next_locs(loc, pipes):
    """Return next legal moves from `loc` in pipes map."""
    moves = {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, -1), (0, 1)],
        'L': [(-1, 0), (0, 1)],
        'J': [(-1, 0), (0, -1)],
        '7': [(1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)],
        '.': [],
        'S': [],
    }
    i, j = loc
    
    return [(i + x[0], j + x[1]) for x in moves[pipes[i][j]]]

def find_start(pipes):
    """Return the location of the `S` node in pipes map."""
    num_rows = len(pipes)
    for i in range(num_rows):
        j = pipes[i].find('S')
        if j != -1:
            return (i, j)

def add_start(graph, pipes):
    """Update (i.e., mutate) graph with next locations from start location."""
    start = find_start(pipes)
    graph[start] = []
    for node in graph:
        if start in graph[node]:
            graph[start].append(node)

    return start

def build_graph(pipes):
    """Return graph with keys 2-tuple location and values list of next locations."""
    graph = {}
    num_rows = len(pipes)
    num_cols = len(pipes[0])
    for i in range(num_rows):
        for j in range(num_cols):
            loc = (i, j)
            next = [(next_loc[0], next_loc[1]) for next_loc in next_locs(loc, pipes)]
            if len(next) > 0:
                graph[loc] = next
    start = add_start(graph, pipes)

    return graph, start

def calc_distances(graph, start):
    """Return dictionary of distances from a start location."""
    distances = {}
    to_visit = [(start, 0)]
    while len(to_visit) > 0:
        next_loc, distance = to_visit.pop(0)
        distances[next_loc] = distance
        to_visit.extend([(node, distance + 1) for node in graph[next_loc]
                            if node not in distances])

    return distances


def occupancy_grid(graph, distances, shape):
    """Expand 2x in horizontal and vertical direction for flood fill."""
    grid = np.zeros(shape, dtype=np.int8)
    for node in distances:
        i, j = node[0], node[1]
        grid[i * 2, j * 2] = 1
        for next in graph[node]:  # connect the pipes in expanded version
            i_p, j_p = next
            grid[i * 2 + i_p - i, j * 2 + j_p - j] = 1

    return np.pad(grid, 2, constant_values=0)

def flood_fill(grid):
    """Flood fill starting at (0, 0)."""
    to_visit = set()
    to_visit.add((0, 0))
    while len(to_visit) > 0:
        loc = to_visit.pop()
        grid[loc[0], loc[1]] = 1
        for next in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i = loc[0] + next[0]
            j = loc[1] + next[1]
            if (i >= 0 and j >= 0 and i < grid.shape[0] and j < grid.shape[1] and
                grid[i, j] == 0):
                to_visit.add((i, j))

    return grid

def main():
    """Load input and call algorithms."""
    pipes = load_input('input.txt')
    graph, start = build_graph(pipes)
    distances = calc_distances(graph, start)
    print(f'Star 1 maximum distance = {max(list(distances.values()))}')
    shape = (len(pipes) * 2, len(pipes[0]) * 2)
    grid = occupancy_grid(graph, distances, shape)
    grid = flood_fill(grid)
    print(f'Star 2 enclosed locations = {(grid[0::2, 0::2] == 0).sum()}')

if __name__ == "__main__":
    main()
