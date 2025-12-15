#!/usr/bin/env python3

import utils

test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def part1(manifold):
    first_beam = manifold[0].index('S')
    beams = [first_beam]
    splits = 0

    for row in manifold[1:]:
        split_beams = []
        for beam in beams:
            if row[beam] == '^':
                split_beams.append(beam - 1)
                split_beams.append(beam + 1)
                splits += 1
            else:
                split_beams.append(beam)
            # remove duplicates & out of bounds beams
        split_beams = [b for b in split_beams if 0 <= b < len(row)]
        beams = list(set(split_beams))

    return splits

def trace_beam(manifold, row, beam, path):
    if beam < 0 or beam >= len(manifold[0]):
        return 0
    if row >= len(manifold):
        print(f"Path: {path}")
        return 1
    if manifold[row][beam] == '^':
        return trace_beam(manifold, row + 1, beam - 1, path + 'A') + trace_beam(manifold, row + 1, beam + 1, path + 'B')
    else:
        return trace_beam(manifold, row + 1, beam, path)

def part2(manifold):
    first_beam = manifold[0].index('S')
    return trace_beam(manifold, 1, first_beam, '')

result = part1(test_input.splitlines())
print("Test Part 1 Result:", result)

result = part1(utils.read_input('day_07.txt'))
print("Part 1 Result:", result)

result = part2(test_input.splitlines())
print("Test Part 2 Result:", result)

result = part2(utils.read_input('day_07.txt'))
print("Part 2 Result:", result)
