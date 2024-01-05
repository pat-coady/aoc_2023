#!/usr/bin/env python3
"""Day 06 Advent of Code."""
import functools
import re


def load_input(filename, star2=False):
    """Return list of 2-tuples with time and record distance."""
    with open(filename) as f:
        line = f.readline().replace(' ', '') if star2 else f.readline()
        times = [int(x) for x in re.findall(r'\d+', line)]
        line = f.readline().replace(' ', '') if star2 else f.readline()
        records = [int(x) for x in re.findall(r'\d+', line)]

    return zip(times, records)


def num_wins(time, record):
    """Return number of winning scenarios."""
    wins = 0
    for t_button in range(time):
        dist = (time - t_button) * t_button
        wins += dist > record

    return wins


def main():
    """Program entry point."""
    for star in [1, 2]:
        races = load_input('input.txt', star == 2)
        win_list = []
        for race in races:
            win_list.append(num_wins(*race))
        win_product = functools.reduce(lambda x, y: x * y, win_list)
        print(f'Star {star} product = {win_product}')


if __name__ == "__main__":
    main()
