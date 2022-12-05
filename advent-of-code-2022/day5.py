"""Advent Of Code 2022 : Day 5
"""
from utils import get_input
from collections import defaultdict


raw_input = get_input(day=5)


def separate_stacks_and_instructions():
    for line_index, line in enumerate(raw_input):
        if line == "":
            raw_stacks = raw_input[:line_index - 1]
            raw_instructions = raw_input[line_index + 1:]
            number_of_columns = int(raw_input[line_index - 1].replace(" ", "")[-1])
            break
    
    stacks = defaultdict(list)
    for stack_line in raw_stacks[::-1]:
        for column_id in range(number_of_columns):
            crate_char = stack_line[column_id * 4 + 1]
            if crate_char == " ":
                continue
            stacks[column_id + 1].append(crate_char)
    
    instructions = [
        instruction_line.split()
        for instruction_line in raw_instructions
    ]
    return stacks, instructions
    


def part1():
    separate_stacks_and_instructions()


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
