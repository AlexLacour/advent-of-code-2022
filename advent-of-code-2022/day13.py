"""Advent Of Code 2022 : Day 13
"""
import math
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
    for left_item_element, right_item_element in zip(left_item, right_item):
        if isinstance(left_item_element, int) and isinstance(right_item_element, int):
            if left_item_element == right_item_element:
                continue
            else:
                return left_item_element < right_item_element

        else:
            if isinstance(left_item_element, int) and isinstance(right_item_element, list):
                left_item_element = [left_item_element]
            elif isinstance(left_item_element, list) and isinstance(right_item_element, int):
                right_item_element = [right_item_element]

            res =  compare_values(left_item_element, right_item_element)
            if res is not None:
                return res
    else:
        if len(left_item) == len(right_item):
            return None
        return len(left_item) < len(right_item)


def part1():
    packets_pairs = get_packets_pairs()

    score = 0
    for pair_id, (left_list, right_list) in enumerate(packets_pairs):
        res = compare_values(left_list, right_list)
        if res is not None:
            score += int(res) * (pair_id + 1)
    return score


def is_list_sorted(packets_list):
    return all(compare_values(item, next_item) for item, next_item in zip(packets_list[:-1], packets_list[1:]))


def part2():
    packets_pairs = get_packets_pairs()
    
    packets = [packet for pair in packets_pairs for packet in pair]
    
    divider_packets = [
        [[2]],
        [[6]]
    ]
    packets.extend(divider_packets)
    
    while not is_list_sorted(packets):
        for item, next_item in zip(packets[:-1], packets[1:]):
            if not compare_values(item, next_item):
                item_index, next_item_index = packets.index(item), packets.index(next_item)
                packets[next_item_index], packets[item_index] = packets[item_index], packets[next_item_index]
    return math.prod([packets.index(packet) + 1 for packet in divider_packets])


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
