#!/usr/bin/env python3

import utils
import functools
import operator

test_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def parse(lines):
	ops = list(lines[-1].split())
	nums = [list(map(int, line.split())) for line in lines[:-1]]
	pivoted = list(map(list, zip(*nums)))
	return (pivoted, ops)

def part1(lines):
	numbers, operators = parse(lines)
	sum = 0
	for i in range(len(numbers)):
		if operators[i] == '+':
			sum += functools.reduce(operator.add, numbers[i])
		else:
			sum += functools.reduce(operator.mul, numbers[i])
	return sum

def rotate_matrix(matrix):
    return [''.join(row) for row in zip(*matrix)][::-1]

def extract_columns(line, widths):
    columns = []
    index = 0
    for width in widths:
        columns.append(line[index:index+width])
        index += width + 1
    return columns

def part2(lines):
	p1, operators = parse(lines)
	print(len(p1), len(lines))
	widths = [len(str(max(p1[i]))) for i in range(len(p1))]
	p2 = [extract_columns(l, widths) for l in lines]
	print(len(p2))
	p3 = list(zip(*p2))
	p4 = [rotate_matrix(m) for m in p3]

	total = 0
	for i in range(len(p4)):
		numbers = [int(i) for i in p4[i]]
		if operators[i] == '+':
			sum = functools.reduce(operator.add, numbers)
		else:
			sum = functools.reduce(operator.mul, numbers)
		total += sum
	return total
	
result = part1(test_input.strip().splitlines())
assert result == 4277556, f"expected 4277556, got {result}"

result = part1(utils.read_input('day_06.txt'))
print('Part 1 -', result)

result = part2(test_input.strip().splitlines())
assert result == 3263827, f"expected 32638272, got {result}"

result = part2(utils.read_input('day_06.txt'))
print('Part 2 -', result)