#!/usr/bin/env python3

import utils

test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def get_point(x, y, grid):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return 0
    return 1 if grid[y][x] == '@' else 0

def get_count_around(x, y, grid):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            count += get_point(x + dx, y + dy, grid)
    return count

def remove_eligible_points(grid):
    new_grid = []
    for y in range(len(grid)):
        new_line = ''
        for x in range(len(grid[0])):
            if get_point(x, y, grid) == 1:
                count = get_count_around(x, y, grid)
                if count < 4:
                    new_line += '.'
                else:
                    new_line += '@'
            else:
                new_line += '.'
        new_grid.append(new_line)
    return new_grid

def part1(lines):
    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if get_point(x, y, lines) == 1:
                count = get_count_around(x, y, lines)
                if count < 4:
                    total += 1
    return total


def part2(lines):
    total = 0
    while part1(lines) > 0:
        total += part1(lines)
        lines = remove_eligible_points(lines)
    return total

test_result = part1(test_input.strip().splitlines())
assert test_result == 13, f"expected 13 but got {test_result}"

result = part1(utils.read_input('day_04.txt'))
print(f"Part 1 - Count of weak signal points: {result}")

test_result = part2(test_input.strip().splitlines())
assert test_result == 43, f"expected 43 but got {test_result}"

result = part2(utils.read_input('day_04.txt'))
print(f"Part 2 - Total removed weak signal points: {result}")