#!/usr/bin/env python3
"""Day 07 Advent of Code."""
from collections import Counter


def card_values(star2):
    """Return dictionary of card values for tie-breakers."""
    if star2:
        cards = ['A', 'K', 'Q', 'T',
                 '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    else:
        cards = ['A', 'K', 'Q', 'J', 'T',
                 '9', '8', '7', '6', '5', '4', '3', '2']
    cards.reverse()
    card_dict = {c: chr(ord('a') + i) for i, c in enumerate(cards)}

    return card_dict


def load_input(filename):
    """Return list of 2-tuples with (hand, bid)."""
    hands = []
    with open(filename) as f:
        for line in f:
            hand, bid = line.rstrip().split(' ')
            hands.append((hand, int(bid)))
    
    return hands


def score_hand(hand, card_dict, star2):
    """Return str representation of hand that sorts in strength-order."""
    counts = Counter(hand)
    score = ''
    if star2:
        js = counts['J']
        counts['J'] = 0
        most_common = counts.most_common(1)[0][0]
        counts[most_common] += js
    for i in range(5, 0, -1):
        score += chr(list(counts.values()).count(i) + ord('a'))
    for c in hand:
        score += card_dict[c]

    return score
    

def main():
    """Load input and call algorithms."""
    hands = load_input('input.txt')
    for star in [1, 2]:
        star2 = star == 2
        card_dict = card_values(star2=star2)
        scored_hands = [(score_hand(hand[0], card_dict, star2=star2), hand)
                        for hand in hands]
        scored_hands.sort(key=lambda x: x[0])
        winnings = 0
        for i, hand in enumerate(scored_hands):
            winnings += (i + 1) * hand[1][1]
        print(f'Star {star} winnings = {winnings}')


if __name__ == "__main__":
    main()
