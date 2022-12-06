"""Advent Of Code 2022 : Day 6
"""
from utils import get_input


raw_input = get_input(day=6)


def part1():
    signal = raw_input[0]
    for char_id, _ in enumerate(signal[:-4]):
        marker = set(signal[char_id:char_id + 4])
        if len(marker) == 4:
            return char_id + 4  # id of the last character of the marker


def part2():
    signal = raw_input[0]
    for char_id, _ in enumerate(signal[:-14]):
        marker = set(signal[char_id:char_id + 14])
        if len(marker) == 14:
            return char_id + 14  # id of the last character of the marker


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
