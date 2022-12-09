"""Advent Of Code 2022 : Day 9
"""
from utils import get_input
import copy
from collections import Counter
import numpy as np


raw_input = get_input(day=9)


directions = {
    "R": np.asarray([0, 1]),
    "L": np.asarray([0, -1]),
    "U": np.asarray([1, 0]),
    "D": np.asarray([-1, 0]),
    "TL": np.asarray([1, -1]),
    "TR": np.asarray([1, 1]),
    "BL": np.asarray([-1, -1]),
    "BR": np.asarray([-1, 1])
}


def get_tail_move(tail, head):
    head_surrounding = set([
        tuple(head),
        *[tuple(head + direction) for direction in directions.values()]
    ])
    
    if tuple(tail) in head_surrounding:
        tail_move = np.array([0, 0])

    elif tail[0] == head[0]:
        tail_move = directions["L"] if head[1] < tail[1] else directions["R"]
        
    elif tail[1] == head[1]:
        tail_move = directions["D"] if head[0] < tail[0] else directions["U"]

    else:
        if head[0] > tail[0]:
            tail_move = directions["TR"] if head[1] > tail[1] else directions["TL"]
        elif head[0] < tail[0]:
            tail_move = directions["BR"] if head[1] > tail[1] else directions["BL"]
        
    return tail_move


def part1():
    start_point = [0, 0]
    
    head_position = np.asarray(copy.deepcopy(start_point))
    tail_position = np.asarray(copy.deepcopy(start_point))

    visited_points = Counter()
    
    visited_points[tuple(start_point)] += 1

    for head_instruction in raw_input:
        direction, distance  = head_instruction.split()
        
        for _ in range(int(distance)):
            # head update
            head_position += directions[direction]

            # tail update
            tail_position += get_tail_move(tail_position, head_position)
            visited_points[tuple(tail_position)] += 1

    return len(visited_points)


def part2():
    start_point = [0, 0]
    
    n_tails = 9
    head_position = np.asarray(copy.deepcopy(start_point))
    tails_position = [np.asarray(copy.deepcopy(start_point)) for _ in range(n_tails)]

    visited_points = Counter()
    
    visited_points[tuple(start_point)] += 1

    for head_instruction in raw_input:
        direction, distance  = head_instruction.split()
        
        for _ in range(int(distance)):
            # head update
            head_position += directions[direction]

            # tails update
            for tail_id, tail_position in enumerate(tails_position):
                if tail_id == 0:
                    new_head_position = head_position
                else:
                    new_head_position = tails_position[tail_id - 1]
                tails_position[tail_id] += get_tail_move(tail_position, new_head_position)

            visited_points[tuple(tails_position[-1])] += 1
    return len(visited_points)


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
