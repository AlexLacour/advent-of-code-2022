"""Advent Of Code 2022 : Day 2
"""
from utils import get_input


raw_input = get_input(day=2)


move_to_action = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


action_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


winning_action = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}


def play_round(opponent_action: str, my_action: str) -> int:
    if opponent_action == my_action:
        return action_score[my_action] + 3
    
    elif winning_action[opponent_action] == my_action:
        return action_score[my_action] + 6
    else:
        return action_score[my_action] + 0


def figure_out_action(opponent_action: str, round_ending: str):
    losing_action = {value: key for key, value in winning_action.items()}
    if round_ending == "X":  # lose
        return losing_action[opponent_action]
    elif round_ending == "Y":  # draw
        return opponent_action
    elif round_ending == "Z":  # win
        return winning_action[opponent_action]


def part1():
    score = 0
    for instruction in raw_input:
        opponent_move, my_move = instruction.split()
        opponent_action = move_to_action[opponent_move]
        my_action = move_to_action[my_move]
        score += play_round(opponent_action, my_action)
    return score


def part2():
    score = 0
    for instruction in raw_input:
        opponent_move, round_ending = instruction.split()
        opponent_action = move_to_action[opponent_move]
        my_action = figure_out_action(opponent_action, round_ending)
        score += play_round(opponent_action, my_action)
    return score


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
