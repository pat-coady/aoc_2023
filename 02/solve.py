#!/usr/bin/env python3
"""Day 02 Advent of Code."""
import functools

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def stars():
    """Star 1 & 2 algorithm."""
    with open('input.txt') as f:
        game_num_sum, power_sum = 0, 0
        for game_num, line in enumerate(f):
            possible = True
            handfuls = line.rstrip().split(': ')[1].split('; ')
            handfuls = [x.split(', ') for x in handfuls]
            min_cubes = {'red': 0, 'green': 0, 'blue': 0}
            for handful in handfuls:
                for cubes in handful:
                    num_cubes, color = cubes.split(' ')
                    num_cubes = int(num_cubes)
                    # star 1
                    if num_cubes > MAX_CUBES[color]:
                        possible = False
                    # star 2
                    min_cubes[color] = max(num_cubes, min_cubes[color])
            if possible:  # star 1
                game_num_sum += game_num + 1
            power_sum += functools.reduce(lambda x, y: x * y, min_cubes.values())  # star 2
    
    return game_num_sum, power_sum

def main():
    """Call star solutions."""
    game_num_sum, power_sum = stars()
    print(f'Star 1 Total = {game_num_sum}')
    print(f'Star 2 Total = {power_sum}')


if __name__ == "__main__":
    main()
