"""Advent Of Code 2022 : Day 8
"""
import numpy as np
from utils import get_input


raw_input = get_input(day=8)


def get_map():
    return np.asarray([[int(tree) for tree in tree_line] for tree_line in raw_input], dtype=np.uint8)


def get_edge_trees(trees_map, line, column) -> list[list[int]]:
    ordered_edges = [
        trees_map[:line, column][::-1],
        trees_map[line + 1:, column],
        trees_map[line, column + 1:],
        trees_map[line, :column][::-1]
    ]
    return ordered_edges


def part1():
    trees_map = get_map()

    visible_trees = 0
    for tree_line_id, tree_line in enumerate(trees_map):
        for tree_id, tree in enumerate(tree_line):
            ordered_edges = get_edge_trees(trees_map, line=tree_line_id, column=tree_id)
            
            if any(
                all(other_tree_value < tree for other_tree_value in edge_trees)
                for edge_trees in ordered_edges
            ) or any(not list(edge_trees) for edge_trees in ordered_edges):
                visible_trees += 1

    return visible_trees


def part2():
    trees_map = get_map()
    
    scenic_scores = []
    for tree_line_id, tree_line in enumerate(trees_map):
        for tree_id, tree in enumerate(tree_line):
            ordered_edges = get_edge_trees(trees_map, line=tree_line_id, column=tree_id)
            
            scenic_score = 1
            for edge_trees in ordered_edges:
                consecutive_smaller_trees = []
                for other_tree in edge_trees:
                    consecutive_smaller_trees.append(other_tree)
                    if other_tree >= tree:
                        break
                scenic_score *= len(consecutive_smaller_trees)
            
            scenic_scores.append(scenic_score)
    return max(scenic_scores)


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
