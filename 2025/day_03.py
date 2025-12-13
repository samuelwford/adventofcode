#!/usr/bin/env python3

import utils

test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

def get_two_batteries(line):
    a = sorted(line[:-1], reverse=True)[0]
    index_of_a = line.index(a)
    b = sorted(line[index_of_a + 1:], reverse=True)[0]
    return int(a + b)

def part1(lines):
    total = 0
    for line in lines:
        total += get_two_batteries(line)
    return total

def turn_off_worst_battery(line):
    best = 0
    for i in range(len(line)):
        modified_line = line[:i] + line[i+1:]
        current_best = int(modified_line)
        if current_best > best:
            best = current_best
    return str(best)

def get_best_twelve_batteries(line):
    while len(line) > 12:
        line = turn_off_worst_battery(line)
    return int(line)

def part2(lines):
    best_batteries = [get_best_twelve_batteries(line) for line in lines]
    return sum(best_batteries)

test_result = part1(test_input.strip().splitlines())
assert test_result == 357, f"expected 357 but got {test_result}"

result = part1(utils.read_input('day_03.txt'))
print(f"Part 1 - Sum of top two batteries: {result}")

test_result = part2(test_input.strip().splitlines())
assert test_result == 3121910778619, f"expected 3121910778619 but got {test_result}"

result = part2(utils.read_input('day_03.txt'))
print(f"Part 2 - Sum of best twelve batteries: {result}")