"""Advent Of Code 2022 : Day 1
"""
from collections import defaultdict
from utils import get_input


raw_input = get_input(day=1)


def part1():
    elves_calories = defaultdict(int)
    
    elf_index = 0
    for calory_str in raw_input:
        if calory_str == "":
            elf_index += 1
        else:
            elves_calories[elf_index] += int(calory_str)
    
    return max(elves_calories.values())

def part2():
    elves_calories = defaultdict(int)
    
    elf_index = 0
    for calory_str in raw_input:
        if calory_str == "":
            elf_index += 1
        else:
            elves_calories[elf_index] += int(calory_str)
    
    return sum(sorted(list(elves_calories.values()))[-3:])


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
