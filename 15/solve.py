#!/usr/bin/env python3
"""Day 15 Advent of Code."""

def load_input(filename):
    """Return list of ascii steps (i.e., the sequence)."""
    with open(filename) as f:
        seq = f.readline().rstrip().split(',')
    
    return seq

def hash_label(label):
    """Return HASH of text label."""
    total = 0
    for c in label:
        total += ord(c)
        total *= 17
        total %= 256

    return total

class Boxes:
    """Object holding 256 boxes with slots to hold lenses."""

    def __init__(self):
        self.boxes = [[] for _ in range(256)]

    def add(self, lens):
        label, power = lens
        loc = self.find(label)
        addr = hash_label(label)
        if loc > -1:
            self.boxes[addr][loc] = lens
        else:
            self.boxes[addr].append(lens)

    def remove(self, label):
        loc = self.find(label)
        addr = hash_label(label)
        if loc > -1:
            self.boxes[addr].pop(loc)

    def find(self, label):
        """Return lens location with same label is present in slot, or -1 if not found."""
        addr = hash_label(label)
        for i, slot in enumerate(self.boxes[addr]):
            label_check, power = slot
            if label_check == label:
                return i
        return -1
    
    def focus_power(self):
        total = 0
        for box in range(256):
            for slot, lens in enumerate(self.boxes[box]):
                label, power = lens
                total += (box + 1) * (slot + 1) * power

        return total

def load_lenses(seq):
    """Return list of 255 lists with lens powers and labels."""
    boxes = Boxes()
    for step in seq:
        if '=' in step:
            label, power = step.split('=')
            lens = (label, int(power))
            boxes.add(lens)
        else:
            label = step.strip('-')
            boxes.remove(label)

    return boxes

def main():
    """Load puzzle input and run algorithms."""
    seq = load_input('input.txt')
    total_hash = 0
    for step in seq:
        total_hash += hash_label(step)
    print(f'Star 1 total HASH = {total_hash}')
    boxes = load_lenses(seq)
    print(f'Total Star 2 focusing power = {boxes.focus_power()}')


if __name__ == "__main__":
    main()
