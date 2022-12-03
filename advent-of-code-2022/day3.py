"""Advent Of Code 2022 : Day 3
"""
from utils import get_input
from collections import Counter


raw_input = get_input(day=3)


def letter_to_score(letter: str) -> int:
    return (ord(letter) - 96) if letter.islower() else (ord(letter) - 64 + 26)


def part1():
    priority_score = 0
    for rucksack in raw_input:
        first_compartment = rucksack[:int(len(rucksack) / 2)]
        second_compartment = rucksack[int(len(rucksack) / 2):]
        
        common_letters = set(first_compartment).intersection(set(second_compartment))
        
        score = 0
        for letter in common_letters:
            score += letter_to_score(letter)

        priority_score += score
        
    return priority_score


def part2():
    priority_score = 0
    for rucksack_group_id in range(len(raw_input) // 3):
        rucksack_group = [
            raw_input[3 * rucksack_group_id],
            raw_input[3 * rucksack_group_id + 1],
            raw_input[3 * rucksack_group_id + 2]
        ]
        
        common_group_letters = list(set(rucksack_group[0]) \
            .intersection(set(rucksack_group[1])) \
            .intersection(set(rucksack_group[2])))
        
        priority_score += letter_to_score(common_group_letters[-1])
    return priority_score


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
