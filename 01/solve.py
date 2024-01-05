#!/usr/bin/env python3
"""Day 01 Advent of Code."""

STAR1 = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}
STAR2 = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def stars(star2=False):
    """Star 1 & Star 2 algorithm."""
    total = 0
    # new language feature in Python 3.9
    # `dict1 | dict2` merges 2 dictionaries
    digits = STAR1 | STAR2 if star2 else STAR1
    first_dig, last_dig = '', ''
    with open('input.txt') as f:
        for line in f:
            first_idx, last_idx = 1000, -1
            for d in digits:
                first, last = line.find(d), line.rfind(d)
                if first != -1 and first < first_idx:
                    first_idx = first
                    first_dig = digits[d]
                if last != -1 and last > last_idx:
                    last_idx = last
                    last_dig = digits[d]   
            total += int(first_dig + last_dig)
    return total

def main():
    """Call star solutions."""
    print(f'Star 1 Total = {stars(star2=False)}')
    print(f'Star 2 Total = {stars(star2=True)}')

if __name__ == "__main__":
    main()
