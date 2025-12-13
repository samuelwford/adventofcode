#!/usr/bin/env python3

import utils

test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def parse(lines):
    ranges = []
    numbers = []
    separator_found = False
    for line in lines:
        line = line.strip()
        if line == "":
            separator_found = True
            continue
        if not separator_found:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            numbers.append(int(line))
    return ranges, numbers

def part1(lines):
    ranges, numbers = parse(lines)
    count = 0
    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                count += 1
                break
    return count

def do_ranges_overlap(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return not (end1 < start2 or end2 < start1)

def combine_ranges(ranges):
    combined = []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    for current in sorted_ranges:
        merged = False
        for i in range(len(combined)):
            if do_ranges_overlap(combined[i], current):
                new_start = min(combined[i][0], current[0])
                new_end = max(combined[i][1], current[1])
                combined[i] = (new_start, new_end)
                merged = True
                break
        if not merged:
            combined.append(current)
    return combined

def part2(lines):
    ranges, _ = parse(lines)
    count = 0
    combined_ranges = combine_ranges(ranges)
    for range in combined_ranges:
        count += range[1] - range[0] + 1
    return count

result = part1(test_input.strip().splitlines())
assert result == 3, f"expected 3 but got {result}"

result = part1(utils.read_input('day_05.txt'))
print(f"Part 1 - Count of numbers in ranges: {result}")

result = part2(test_input.strip().splitlines())
assert result == 14, f"expected 14 but got {result}"

result = part2(utils.read_input('day_05.txt'))
print(f"Part 2 - Total range coverage: {result}")