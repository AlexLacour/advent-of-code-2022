"""Advent Of Code 2022 : Day 12
"""
import copy

from utils import get_input
import numpy as np


raw_input = get_input(day=12)

move_set = [
    np.asarray([0, 1]),  # R
    np.asarray([0, -1]),  # L
    np.asarray([1, 0]),  # D
    np.asarray([-1, 0])  # U
]


neighbors_memory = {}


def get_map():
    start_point = None
    end_point = None
    for line_id, line in enumerate(raw_input):
        for col_id, element in enumerate(line):
            if element == "S":
                start_point = (line_id, col_id)
            elif element == "E":
                end_point = (line_id, col_id)

    input_to_int = np.asarray([
        [ord(char) - 96 for char in line.replace("S", "a").replace("E", "z")]
        for line in raw_input
    ], dtype=int)
    return start_point, end_point, input_to_int


def find_possible_moves(point, height_map):
    if point not in neighbors_memory:
        possible_moves = [
            tuple(point + move)
            for move in move_set
            if not any(value < 0 for value in tuple(point + move)) \
               and not tuple(point + move)[0] >= len(height_map) and not tuple(point + move)[1] >= len(height_map[0]) \
               and height_map[tuple(point + move)] - height_map[point] <= 1 \
        ]
        neighbors_memory[point] = possible_moves

    return neighbors_memory[point]


def find_moves_leading_to(point, height_map):
    leading_moves = []
    for line_id, line in enumerate(height_map):
        for col_id, _ in enumerate(line):
            if point in find_possible_moves((line_id, col_id), height_map):
                leading_moves.append((line_id, col_id))
    return leading_moves


def get_distances_from(start_point, height_map, from_the_end: bool = False):
    unvisited = {(line_id, col_id) for line_id, line in enumerate(height_map) for col_id, _ in enumerate(line)}
    distances = {point: np.inf for point in unvisited}
    distances[start_point] = 0

    while unvisited:
        current_node = min(list(unvisited), key=distances.get)

        if not from_the_end:
            neighbors = find_possible_moves(current_node, height_map)
        else:
            neighbors = find_moves_leading_to(current_node, height_map)

        for neighbor_point in neighbors:
            if distances[current_node] + 1 <= distances[neighbor_point]:
                distances[neighbor_point] = distances[current_node] + 1

        unvisited.remove(current_node)
    return distances


def part1():
    start_point, end_point, height_map = get_map()

    distances = get_distances_from(start_point, height_map)

    return distances[end_point]


def part2():
    _, end_point, height_map = get_map()

    distances = get_distances_from(end_point, height_map, from_the_end=True)

    potential_starts = [
        (line_id, col_id)
        for line_id, line in enumerate(raw_input)
        for col_id, element in enumerate(line)
        if element == "a" and (line_id, col_id)
    ]

    start_distances = [distances[point] for point in potential_starts]
    return min(start_distances)


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
