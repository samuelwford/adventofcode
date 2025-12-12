#!/usr/bin/env python3

import utils

test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def parse(lines):
    return [tuple(map(int, line.split('-'))) for line in lines.split(',')]

def chunks_of(s, size):
    for i in range(0, len(s), size):
        yield s[i:i+size]

def repeats_twice(n):
    s = str(n)
    l = len(s)
    if l % 2 == 0 and s[0:l//2] == s[l//2:l]:
        return True
    return False

def repeats(n):
    s = str(n)
    l = len(s)
    for size in range(1, l//2 + 1):
        chunks = list(chunks_of(s, size))
        if all(c == chunks[0] for c in chunks):
            return True
    return False

def part1(ranges):
    sum = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if repeats_twice(i):
                sum += i
    return sum

def part2(ranges):
    sum = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if repeats(i):
                sum += i
    return sum

test_ranges = parse(test_input)

test_result = part1(test_ranges)
assert test_result == 1227775554, f"expected 1227775554, got {test_result}"
test_result = part2(test_ranges)
assert test_result == 4174379265, f"expected 4174379265, got {test_result}"

ranges = parse(utils.read_input('day_02.txt')[0])

result = part1(ranges)
print(f"Part 1 - Sum of invalid numbers: {result}")

result = part2(ranges)
print(f"Part 2 - Sum of invalid numbers: {result}")