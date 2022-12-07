"""Advent Of Code 2022 : Day 7
"""
from utils import get_input
from collections import defaultdict


raw_input = get_input(day=7)


def get_file_system_architecture():
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
                    system_subdict = system
                    for dir_name in current_dir[:-1]:
                        system_subdict = system_subdict[dir_name]
                    if current_dir[-1] not in system_subdict:
                        system_subdict[current_dir[-1]] = {}
            elif split_line[1] == "ls":
                for ls_line in raw_input[line_id + 1:]:
                    if ls_line.startswith("$"):
                        break
                    split_ls_line = ls_line.split()
                    if not ls_line.startswith("dir"):
                        system_subdict = system
                        for dir_name in current_dir[:-1]:
                            system_subdict = system_subdict[dir_name]
                        system_subdict[current_dir[-1]][split_ls_line[1]] = int(split_ls_line[0])

    return system


def get_folder_size(system_dict, folder_size_memory):
    size = 0
    for sub_name, content in system_dict.items():
        size += content if isinstance(content, int) else get_folder_size(content, folder_size_memory)

    folder_size_memory.append(size)

    return size


def part1():
    system = get_file_system_architecture()

    folder_size = []
    _ = get_folder_size(system, folder_size)

    return sum([value for value in folder_size if value <= 100000])


def part2():
    system = get_file_system_architecture()

    folder_size = []
    total = get_folder_size(system, folder_size)

    unused_space = 70_000_000 - total
    needed_space = 30_000_000 - unused_space

    return min([value for value in folder_size if value >= needed_space])


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
