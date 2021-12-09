#!/usr/bin/env python3

import utils

lines = utils.read_input('day_09.txt')
# lines = [
#     "2199943210",
#     "3987894921",
#     "9856789892",
#     "8767896789",
#     "9899965678",
# ]

def find_low_points(grid):
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_low_point(grid, x, y):
                low_points.append(number_at(grid, x, y))
    return low_points

def is_low_point(grid, x, y):
    p = number_at(grid, x, y)
    surrounding_points = [
        number_at(grid, x - 1, y),
        number_at(grid, x + 1, y),
        number_at(grid, x, y - 1),
        number_at(grid, x, y + 1),
    ]
    is_low = True
    for sp in surrounding_points:
        if sp > -1 and p >= sp:
            is_low = False
    return is_low

def number_at(grid, x, y):
    if x > -1 and x < len(grid[0]) and y > -1 and y < len(grid):
        return int(grid[y][x])
    else:
        return -1

low_points = find_low_points(lines)
risk_levels = [p + 1 for p in low_points]
sum_of_risk_levels = sum(risk_levels)

print('part 1 - sum of risk levels', sum_of_risk_levels)

def fill_basins(grid):
    sx = len(grid[0])
    sy = len(grid)
    basins = [[0 for x in range(sx)] for y in range(sy)]
    for y in range(sy):
        for x in range(sx):
            if number_at(grid, x, y) == 9:
                basins[y][x] = -1
    basin = 0
    for y in range(sy):
        for x in range(sx):
            if basins[y][x] == 0:
                basin += 1
                fill_basin(basins, x, y, basin)
    return basins

def fill_basin(grid, x, y, basin):
    for delta in [-1, 1]:        
        if number_at(grid, x + delta, y) == 0:
            grid[y][x + delta] = basin
            fill_basin(grid, x + delta, y, basin)
        if number_at(grid, x, y + delta) == 0:
            grid[y + delta][x] = basin
            fill_basin(grid, x, y + delta, basin)

basins = fill_basins(lines)
basin_sizes = {}
for row in basins:
    for val in row:
        if val > -1:
            if val in basin_sizes:
                basin_sizes[val] += 1
            else:
                basin_sizes[val] = 1
top_three = sorted(basin_sizes.values())[-3:]

from functools import reduce
product = reduce(lambda a, b: a * b, top_three)

print('part 2 - product of size of three largest basins', product)