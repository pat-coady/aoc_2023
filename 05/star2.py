#!/usr/bin/env python3
"""Day 05 Advent of Code - Star 2."""
import re


def load_input(filename):
    """Parse input file and return list of seeds and list of maps."""
    with open(filename) as f:
        maps = []
        seed_ranges = []
        seeds = re.findall(r'\d+', f.readline())
        for i in range(len(seeds) // 2):
            start = int(seeds[i * 2])
            range_len = int(seeds[i * 2 + 1])
            seed_ranges.append((start, start + range_len - 1))
        f.readline()
        for line in f:
            if 'map' in line:
                mapping = []
            elif len(line) < 3:
                maps.append(mapping)
            else:
                dest, source, range_len = (int(x) for x in re.findall(r'\d+', line))
                offset = dest - source
                src1, src2 = source, source + range_len - 1
                mapping.append(((src1, src2), offset))
        maps.append(mapping)

    return seed_ranges, maps


def translate_range(seeds, mapping):
    """Pass input range through mapping."""
    ((src1, src2), offset) = mapping
    no_match = []
    translated = []
    for seed in seeds:
        s1, s2 = seed  # unpack start and end of seed locations
        no_match.append((s1, min(s2, src1 - 1)))
        no_match.append((max(s1, src2 + 1), s2))
        translated.append((max(s1, src1) + offset, min(s2, src2) + offset))
    no_match = list(filter(lambda x: x[0] <= x[1], no_match))
    translated = list(filter(lambda x: x[0] <= x[1], translated))
    
    return no_match, translated


def main():
    """Entry point."""
    filename = 'input.txt'
    seed_ranges, maps = load_input(filename)
    next_ranges = seed_ranges.copy()
    for map in maps:
        current_ranges = next_ranges
        next_ranges = []
        for mapping in map:
            no_match, translated = translate_range(current_ranges, mapping)
            next_ranges.extend(translated)
            current_ranges = no_match
        next_ranges.extend(current_ranges)
    print(f'Star 2 minimum location: {min(list(zip(*next_ranges))[0])}')
    

if __name__ == "__main__":
    main()
