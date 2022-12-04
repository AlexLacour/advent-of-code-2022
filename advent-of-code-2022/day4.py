"""Advent Of Code 2022 : Day 4
"""
from utils import get_input


raw_input = get_input(day=4)


def assignment_to_sets(assignment: str):
    first_sections, second_sections = assignment.split(",")
        
    first_sections_start, first_sections_end = first_sections.split("-")
    second_sections_start, second_sections_end = second_sections.split("-")
    
    first_sections_set = set(range(int(first_sections_start), int(first_sections_end) + 1))
    second_sections_set = set(range(int(second_sections_start), int(second_sections_end) + 1))
    
    return first_sections_set, second_sections_set


def part1():
    full_overlap_counter = 0
    for assignment in raw_input:
        first_sections_set, second_sections_set = assignment_to_sets(assignment)
        
        if first_sections_set.issubset(second_sections_set) or second_sections_set.issubset(first_sections_set):
            full_overlap_counter += 1
    return full_overlap_counter


def part2():
    partial_overlap_counter = 0
    for assignment in raw_input:
        first_sections_set, second_sections_set = assignment_to_sets(assignment)
        
        if first_sections_set.intersection(second_sections_set):
            partial_overlap_counter += 1
    return partial_overlap_counter


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
