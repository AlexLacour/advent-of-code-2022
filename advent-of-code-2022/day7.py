"""Advent Of Code 2022 : Day 7
"""
from utils import get_input
from collections import defaultdict


raw_input = get_input(day=7)


def get_file_system_architecture() -> dict:
    current_dir = []
    system = {}
    for line_id, line in enumerate(raw_input):
        split_line = line.split()
        if split_line[0] == "$":  # instruction
            if split_line[1] == "cd":
                if split_line[-1] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(split_line[-1])
                    if split_line[-1] not in system:
                        system[split_line[-1]] = {}
            elif split_line[1] == "ls":
                for ls_line in raw_input[line_id + 1:]:
                    if ls_line.startswith("$"):
                        break
                    split_ls_line = ls_line.split()
                    if ls_line.startswith("dir"):
                        system[split_ls_line[-1]] = {}
                    else:
                        system[current_dir[-1]][split_ls_line[1]] = int(split_ls_line[0])
                        
    return system


def folder_size(system_dict: dict) -> dict:
    folder_size_int = 0
    for key, value in system_dict.items():
        if isinstance(value, dict):
            folder_size_int += folder_size(value)
            return folder_size_int
        else:
            return value


def part1():
    system = get_file_system_architecture()
    
    return folder_size(system)


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
