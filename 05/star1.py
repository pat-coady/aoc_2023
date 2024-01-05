#!/usr/bin/env python3
"""Day 05 Advent of Code - Star 1."""
import re


class Mapping:
    """Object to store source to destination mapping."""

    def __init__(self, source, dest, range_len):
        self.source = source
        self.dest = dest
        self.range_len = range_len

    def __contains__(self, location):
        """Return True if location resides in source range."""
        return (location >= self.source and
                location < self.source + self.range_len)
    
    def __str__(self):
        """Printable version of mapping."""
        return f's:{self.source}, d:{self.dest}, r:{self.range_len}'
    
    def destination(self, loc):
        return loc + self.dest - self.source



def load_input(filename):
    """Parse input file and return list of seeds and list of maps."""
    with open(filename) as f:
        maps = []
        seeds = re.findall(r'\d+', f.readline())
        f.readline()
        for line in f:
            if 'map' in line:
                mapping = []
            elif len(line) < 3:
                maps.append(mapping)
            else:
                dest, source, range_len = (int(x) for x in re.findall(r'\d+', line))
                mapping.append(Mapping(source, dest, range_len))
        maps.append(mapping)

    return seeds, maps


def find_loc(seed, maps):
    """Trace through map and return seed location."""
    loc = seed
    for mapping in maps:
        for m in mapping:
            if loc in m:
                loc = m.destination(loc)
                break

    return loc


def main():
    """Call sub-algorithms."""
    filename = 'input.txt'
    seeds, maps = load_input(filename)
    locs = []
    for seed in seeds:
        locs.append(find_loc(int(seed), maps))
    print(f'Star 1 minimum location: {min(locs)}')


if __name__ == "__main__":
    main()
