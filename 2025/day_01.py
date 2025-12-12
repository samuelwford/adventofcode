#!/usr/bin/env python3

from functools import reduce
import utils

def part1(state, turn):
    dial, rotations = state
    direction, distance = turn
    
    if direction == 'L':
        dial = dial - distance
        while dial < 0:
            dial = 100 - abs(dial)
    else:
        dial = dial + distance
        while dial >= 100:
            dial = dial - 100

    if dial == 0:
        rotations += 1

    return (dial, rotations)

def part2(turns):
    position = 50
    count = 0

    for direction, distance in turns:
        if direction == 'L':
            # Count how many times we cross 0 going left
            for step in range(1, distance + 1):
                new_pos = (position - step) % 100
                if new_pos == 0:
                    count += 1
            position = (position - distance) % 100
        else:  # 'R'
            # Count how many times we cross 0 going right
            for step in range(1, distance + 1):
                new_pos = (position + step) % 100
                if new_pos == 0:
                    count += 1
            position = (position + distance) % 100
    
    return count

def parse(lines):
    return [(line[0], int(line[1:])) for line in lines]

test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
turns = parse(test_input.strip().split('\n')) 

result = reduce(part1, turns, (50, 0))
assert result == (32, 3), 'expected (32, 3), got {}'.format(result)
result = part2(turns)
assert result == 6, 'expected 6, got {}'.format(result)

turns = parse(utils.read_input('day_01.txt'))

result = reduce(part1, turns, (50, 0))
print(f"Part 1 - Final dial position: {result[0]}, Total rotations: {result[1]}")
result = part2(turns)
print(f"Part 2 - Total rotations: {result}")