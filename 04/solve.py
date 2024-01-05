#!/usr/bin/env python3
"""Day 04 Advent of Code."""
import re

import numpy as np


def matches(filename):
    """Calculate number of matches per card."""
    game_matches = []
    with open(filename) as f:
        for line in f:
            line = line.split(': ')[1]  # remove game num
            my_nums, win_nums = line.split('|')
            my_nums = {x for x in re.findall(r'\d+', my_nums)}
            win_nums = {x for x in re.findall(r'\d+', win_nums)}
            game_matches.append(len(my_nums.intersection(win_nums)))
    
    return np.array(game_matches)

def star2(game_matches):
    """Star 2 algorithm."""
    num_cards = np.ones_like(game_matches)
    for i, num_matches in enumerate(game_matches):
        num_cards[i + 1:i + 1 + num_matches] += num_cards[i]
    
    return num_cards.sum()

def main():
    """Call star solutions."""
    filename = 'input.txt'
    game_matches = matches(filename)
    star1 = np.power(2, game_matches) * (game_matches > 0) / 2
    print(f'Star 1 total = {int(star1.sum())}')
    num_cards = np.ones_like(game_matches)
    for i, num_matches in enumerate(game_matches):
        num_cards[i + 1:i + 1 + num_matches] += num_cards[i]
    print(f'Star 2 total = {star2(game_matches)}')


if __name__ == "__main__":
    main()
