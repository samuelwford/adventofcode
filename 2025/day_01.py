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

    print(f"After turn {turn}, dial is at {dial} with {rotations} rotations")
    return (dial, rotations)

def part2(state, turn):
    dial, rotations = state
    direction, distance = turn
    
    print("\n-----")
    print(f"Starting turn {turn} from dial {dial} with {rotations} rotations")

    if direction == 'L':
        if dial == 0:
            dial = 100 # Start from 100 if at 0 and turning left
        dial -= distance
        print(f"Turning left {distance} from {dial + distance} to {dial}")
        while dial < 0:
            dial = 100 + dial
            rotations += 1 if dial != 0 else 0
            print("Completed a rotation going left ending at ", dial)
    else:
        dial += distance
        print(f"Turning right {distance} from {dial - distance} to {dial}")
        while dial > 99:
            dial -= 100
            rotations += 1 if dial != 0 else 0
            print("Completed a rotation going right ending at ", dial)

    if dial == 0:
        print("Dial hit zero!")
        rotations += 1

    print(f"After turn {turn}, dial is at {dial} with {rotations} rotations")
    readline = input("Press Enter to continue...")

    return (dial, rotations)

turns = [(line[0], int(line[1:])) for line in utils.read_input('day_01.txt')]

# x = part2((50, 0), ('L', 68))
# x = part2(x, ('L', 30))
# x = part2(x, ('R', 48))
# x = part2(x, ('L', 5))
# x = part2(x, ('R', 60))
# x = part2(x, ('L', 55))
# x = part2(x, ('L', 1))
# x = part2(x, ('L', 99))
# x = part2(x, ('R', 14))
# x = part2(x, ('L', 82))

# reduce(part1, turns, (50, 0))
reduce(part2, turns, (50, 0))