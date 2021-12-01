#!/usr/bin/env python3

import utils

depths = [int(line) for line in utils.read_input('day_01.txt')]

diffs = [b - a for (a, b) in zip(depths[:-1], depths[1:])]
incs = sum(1 for d in diffs if d > 0)

print("part 1 - increases:", incs)

windows = [sum(depths[i:i+3]) for i in range(len(depths) - 2)]
diffs = [b - a for (a, b) in zip(windows[:-1], windows[1:])]
incs = sum(1 for d in diffs if d > 0)

print("part 2 - increases:", incs)
