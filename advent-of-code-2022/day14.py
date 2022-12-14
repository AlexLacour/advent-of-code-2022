"""Advent Of Code 2022 : Day 14
"""
from utils import get_input
import numpy as np


raw_input = get_input(day=14)


def get_points_between(point_a, point_b):
    if point_a[0] == point_b[0]:
        if point_a[1] < point_b[1]:
            base_coordinate, end_coordinate = point_a[1], point_b[1]
        else:
            base_coordinate, end_coordinate = point_b[1], point_a[1]
        return [(point_a[0], base_coordinate + point_id) for point_id in
                range(end_coordinate - base_coordinate + 1)]
    else:
        if point_a[0] < point_b[0]:
            base_coordinate, end_coordinate = point_a[0], point_b[0]
        else:
            base_coordinate, end_coordinate = point_b[0], point_a[0]
        return [(base_coordinate + point_id, point_a[1]) for point_id in
                range(end_coordinate - base_coordinate + 1)]


def get_paths():
    paths = []
    for line in raw_input:
        anchor_points = [tuple(int(value) for value in point.split(",")) for point in line.split(" -> ")]

        points = set([
            line_point for point, next_point in zip(anchor_points[:-1], anchor_points[1:])
            for line_point in get_points_between(point, next_point)
        ])

        paths.append(points)
    return paths


moves = [
    np.asarray([0, 1]),
    np.asarray([-1, 1]),
    np.asarray([1, 1])
]
sand_possible_positions_memory = {}

def get_sand_possible_positions(sand_position):
    if sand_position not in sand_possible_positions_memory:
        sand_possible_positions_memory[sand_position] = [
            tuple(sand_position + move)
            for move in moves
        ]
    return sand_possible_positions_memory[sand_position]


def part1():
    paths = get_paths()

    rock_points = set([point for path in paths for point in path])
    rock_bottom = max(rock_points, key=lambda rock_point: rock_point[1])[1]

    sand_start_point = (500, 0)

    sand_points = set()
    while True:
        sand_position = sand_start_point
        while True:
            sand_possible_positions = get_sand_possible_positions(sand_position)

            next_sand_position = None
            for sand_possible_position in sand_possible_positions:
                if sand_possible_position not in rock_points and sand_possible_position not in sand_points:
                    next_sand_position = sand_possible_position
                    break
            if next_sand_position is None:
                sand_points.add(sand_position)
                break

            sand_position = next_sand_position
            if sand_position[1] > rock_bottom:
                return len(sand_points)


def part2():
    paths = get_paths()

    rock_points = set([point for path in paths for point in path])
    rock_bottom = max(rock_points, key=lambda rock_point: rock_point[1])[1]

    sand_start_point = (500, 0)

    sand_points = set()
    while True:
        sand_position = sand_start_point
        while True:
            sand_possible_positions = get_sand_possible_positions(sand_position)

            next_sand_position = None
            for sand_possible_position in sand_possible_positions:
                if sand_possible_position not in rock_points and sand_possible_position not in sand_points:
                    next_sand_position = sand_possible_position
                    break
            if next_sand_position is None:
                sand_points.add(sand_position)
                if sand_position == sand_start_point:
                    return len(sand_points)
                break

            if next_sand_position[1] == rock_bottom + 2:
                sand_points.add(sand_position)
                break

            sand_position = next_sand_position


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
