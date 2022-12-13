"""Advent Of Code 2022 : Day 13
"""
from utils import get_input
import json


raw_input = get_input(day=13)


def get_packets_pairs():
    packets_pairs = []
    for line, next_line in zip(raw_input[:-1], raw_input[1:]):
        if line and next_line:
            packets_pairs.append((json.loads(line), json.loads(next_line)))
    return packets_pairs


def compare_values(left_item: list, right_item: list):
    comparisons = []

    print(left_item, right_item)

    for left_item_element, right_item_element in zip(left_item, right_item):
        print(left_item_element, right_item_element)
        if isinstance(left_item_element, int) and isinstance(right_item_element, int):
            if left_item_element == right_item_element:
                continue
            else:
                res = left_item_element < right_item_element
                comparisons.append(res)
                if res:
                    print("We good, right > left")
                else:
                    print("We bad, right < left")
                return res

        else:
            if isinstance(left_item_element, int) and isinstance(right_item_element, list):
                left_item_element = [left_item_element]
            elif isinstance(left_item_element, list) and isinstance(right_item_element, int):
                right_item_element = [right_item_element]

            return compare_values(left_item_element, right_item_element)

    if not comparisons:
        if len(left_item) == len(right_item):
            print("lists are the same length")
            return None
        res = len(left_item) < len(right_item)
        if res:
            print("We good, left ran out first")
        else:
            print("We bad, right ran out first")
        return res

    # return all(value for value in comparisons)


def part1():
    packets_pairs = get_packets_pairs()

    score = 0
    for pair_id, (left_list, right_list) in enumerate(packets_pairs):
        res = compare_values(left_list, right_list)
        print()
        if res is not None:
            score += int(res) * (pair_id + 1)
    return score


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
