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
	ops = list(lines.pop().split())
	nums = [list(map(int, line.split())) for line in lines]
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
	
result = part1(test_input.strip().splitlines())
assert result == 4277556, f"expected 4277556, got {result}"

result = part1(utils.read_input('day_06.txt'))
print('Part 1 -', result)
