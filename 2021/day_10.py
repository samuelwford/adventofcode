#!/usr/bin/env python3

import utils

lines = utils.read_input('day_10.txt')

def parse(line):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        else:
            m = stack.pop()
            e = pairs[m]
            if c != e:
                return (False, c)
    closing = [pairs[s] for s in stack]
    return (True, ''.join(closing[::-1]))

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
counts = {')': 0, ']': 0, '}': 0, '>': 0}
for line in lines:
    ok, c = parse(line)
    if not ok:
        counts[c] += 1

total = 0
for s in counts:
    total += counts[s] * points[s]

print('part 1 - total', total)

points = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in lines:
    ok, c = parse(line)
    if ok:
        score = 0
        for s in c:
            score = score * 5 + points[s]
        scores.append(score)
        
import statistics
print('part 2 - middle score', statistics.median(scores))

