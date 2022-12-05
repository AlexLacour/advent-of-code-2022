"""Advent Of Code 2022 : Day 5
"""
from utils import get_input
from collections import defaultdict


raw_input = get_input(day=5)


def parse_instruction(instruction_line_str: str):
    split_instruction = instruction_line_str.split()
    return list(map(int, [split_instruction[1], split_instruction[3], split_instruction[5]]))


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
        parse_instruction(instruction_line)
        for instruction_line in raw_instructions
    ]
    return stacks, instructions


def part1():
    stacks, instructions = separate_stacks_and_instructions()

    for instruction in instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2]].append(stacks[instruction[1]].pop())
    return "".join([stack[-1] for stack in stacks.values()])


def part2():
    stacks, instructions = separate_stacks_and_instructions()

    for instruction in instructions:
        crates = [stacks[instruction[1]].pop() for _ in range(instruction[0])][::-1]
        stacks[instruction[2]].extend(crates)

    return "".join([stack[-1] for stack in stacks.values()])


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
