"""Advent Of Code 2022 : Day 10
"""
from collections import defaultdict
import queue
from utils import get_input
import numpy as np


raw_input = get_input(day=10)


def run_instructions():
    signal = []
    
    signal.append(1)
    
    for instruction in raw_input:
        if instruction != "noop":
            value_to_add = int(instruction.split()[-1])
            signal.extend([signal[-1], signal[-1] + value_to_add])
        else:
            signal.append(signal[-1])
    return signal


def part1():    
    signal = run_instructions()
    
    signal_idxs = [20, 60, 100, 140, 180, 220]
    
    return sum([idx * signal[idx - 1] for idx in signal_idxs])


def render_screen(raw_screen):
    screen = np.reshape(raw_screen, (6, 40))
    rendered_screen = "\n".join([
        "".join([u"\u2588" if value else " " for value in row])
        for row in screen
    ])
    return "\n" + rendered_screen


def part2():
    raw_screen = np.zeros((6 * 40))
    
    for cycle_id, signal_value in enumerate(run_instructions()):
        sprite = range(signal_value - 1, signal_value + 2)
        if cycle_id % 40 in sprite:
            raw_screen[cycle_id] = 1
    return render_screen(raw_screen)


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
