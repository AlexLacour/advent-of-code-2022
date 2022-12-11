"""Advent Of Code 2022 : Day 11
"""
from collections import defaultdict
import copy
import sys
from utils import get_input
import math


raw_input = get_input(day=11)


class StupidMonkey:
    def __init__(self, monkey_id: int, items: list, operation_str: str, test_str: str, next_throw: tuple,
                 boredom: int):
        self.monkey_id = monkey_id
        self.items = items
        self.operation_str = operation_str
        self.operation = self.operation_str.split(" = ")[-1]
        self.test_str = test_str
        self.next_throw = next_throw
        self.boredom = boredom
        self.inspection_counter = 0
    
    def __repr__(self) -> str:
        return str(self.inspection_counter)
    
    def receive_items(self, item_levels: list[int]):
        self.items.extend(item_levels)

    @staticmethod
    def execute_operation(operation, item_level: int) -> int:
        operation_lambda_str = f"lambda old: {operation}"
        new_item_level = eval(operation_lambda_str)(item_level)
        return new_item_level

    def get_divisible_by(self):
        return int(self.test_str.split(" by ")[-1])

    def execute_test(self, item_level: int) -> bool: 
        if "divisible" in self.test_str:
            divisible_by = self.get_divisible_by()

            if item_level % divisible_by == 0:
                return True
            return False
        else:
            raise Exception(f"new test found {self.test_str}")

    def get_next_throws(self):
        next_items_thrown = defaultdict(list)
        for item_level in copy.deepcopy(self.items):

            # V1 (the long way round)
            new_item_level = self.execute_operation(self.operation, item_level)
            if self.boredom > 1:
                new_item_level //= self.boredom
            new_item_level = new_item_level % math.prod([monkey.get_divisible_by() for monkey in get_monkeys(self.boredom)])
            item_test_result = self.execute_test(new_item_level)

            if item_test_result:
                next_items_thrown[self.next_throw[0]].append(new_item_level)
            else:
                next_items_thrown[self.next_throw[1]].append(new_item_level)

            self.items.pop(0)
            self.inspection_counter += 1
        return next_items_thrown


class Monkey:
    def __init__(self, monkey_id: int, items: list, operation_str: str, test_str: str, next_throw: tuple,
                 boredom: int):
        self.monkey_id = monkey_id
        self.items = items
        self.operation_str = operation_str
        self.operation = self.operation_str.split(" = ")[-1]
        self.test_str = test_str
        self.next_throw = next_throw
        self.boredom = boredom
        self.inspection_counter = 0
    
    def __repr__(self) -> str:
        return str(self.inspection_counter)
    
    def receive_items(self, item_levels: list[int]):
        self.items.extend(item_levels)

    def get_divisible_by(self):
        return int(self.test_str.split(" by ")[-1])

    def get_next_throws(self):
        next_items_thrown = defaultdict(list)
        for item_level in copy.deepcopy(self.items):
            _, operator, operand2 = self.operation.split()
            operand2 = operand2 if operand2.isdigit() else item_level
            
            n = self.get_divisible_by()
            
            a = item_level
            _, b = divmod(a, n)  # congruence(a)
            
            if operator == "+":
                # (a + a2) / k ≡ (b + b2) / k (mod n)
                a2 = int(operand2)
                _, b2 = divmod(a2, n)
                
                congruence_value = (b + b2)

            elif operator == "*":
                # a.a2 / k ≡ b.b2 / k (mod n)
                a2 = int(operand2)
                _, b2 = divmod(a2, n)
                
                congruence_value = (b * b2)

            item_test = congruence_value == 0
            
            computed_value = n + congruence_value  # todo multiply n

            if item_test:  # divisible
                next_items_thrown[self.next_throw[0]].append(computed_value)
            else:
                next_items_thrown[self.next_throw[1]].append(computed_value)

            self.items.pop(0)
            self.inspection_counter += 1
        return next_items_thrown


def get_monkeys(boredom_level: int = 3) -> list[Monkey]:
    monkeys = []
    for line_id, line in enumerate(raw_input):
        if line.startswith("Monkey"):  # init new monkey
            monkeys.append(StupidMonkey(
                monkey_id=int("".join(line.split()[1][:-1])),
                items=list(map(int, raw_input[line_id + 1].split(": ")[-1].split(","))),
                operation_str=raw_input[line_id + 2].split(": ")[-1],
                test_str=raw_input[line_id + 3].split(": ")[-1],
                next_throw=(
                    int(raw_input[line_id + 4].split(": ")[-1].split()[-1]),
                    int(raw_input[line_id + 5].split(": ")[-1].split()[-1])
                ),
                boredom=boredom_level
            ))
    return monkeys


def part1():
    monkeys = get_monkeys(boredom_level=3)
    
    n_rounds = 20
    
    for _ in range(n_rounds):
        for monkey in monkeys:
            next_items_thrown = monkey.get_next_throws()
            for monkey_id, new_items in next_items_thrown.items():
                monkeys[monkey_id].receive_items(new_items)

    print([monkey.items for monkey in monkeys])

    busy_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspection_counter)[-2:]

    return math.prod([monkey.inspection_counter for monkey in busy_monkeys])
    

def part2():
    monkeys = get_monkeys(boredom_level=1)
    
    n_rounds = 10_000
    
    for round_id in range(n_rounds):
        for monkey in monkeys:
            next_items_thrown = monkey.get_next_throws()
            for monkey_id, new_items in next_items_thrown.items():
                monkeys[monkey_id].receive_items(new_items)

    busy_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspection_counter)[-2:]
    return math.prod([monkey.inspection_counter for monkey in busy_monkeys])


if __name__ == "__main__":
    print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
