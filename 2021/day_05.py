#!/usr/bin/env python3

import re
import utils

#lines = utils.read_input('day_05_sample.txt')
lines = utils.read_input('day_05.txt')

t = [re.search(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in lines]
coords = [tuple(int(j) for j in i) for i in t]

max_x = max([max(x1, x2) for x1, y1, x2, y2 in coords]) + 1
max_y = max([max(y1, y2) for x1, y1, x2, y2 in coords]) + 1

def pretty_print(grid):
    print('-----')
    for y in range(max_y):
        for x in range(max_x):
            c = grid[y][x]
            print(f"{c:3}", end =" ")
        print()

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def between(i, a, b):
    return i >= min(a, b) and i <= max(a, b)
    
def line(g, x1, y1, x2, y2):
    cx, cy = x1, y1
    dx = sign(x2 - x1)
    dy = sign(y2 - y1)
    while between(cx, x1, x2) and between(cy, y1, y2):
        g[cy][cx] += 1
        cx += dx
        cy += dy
    
grid = []
for y in range(max_y):
    grid.append([])
    for x in range(max_x):
        grid[y].append(0)

for (x1, y1, x2, y2) in coords:
    if x1 == x2 or y1 == y2:
        line(grid, x1, y1, x2, y2)

overlaps = 0
for y in range(max_y):
    for x in range(max_x):
        if grid[y][x] > 1:
            overlaps += 1

print('part 1 - overlaps:', overlaps)

grid = []
for y in range(max_y):
    grid.append([])
    for x in range(max_x):
        grid[y].append(0)

for (x1, y1, x2, y2) in coords:
    line(grid, x1, y1, x2, y2)

overlaps = 0
for y in range(max_y):
    for x in range(max_x):
        if grid[y][x] > 1:
            overlaps += 1

print('part 2 - overlaps:', overlaps)
