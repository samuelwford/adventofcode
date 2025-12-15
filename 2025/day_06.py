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
    x = [''.join(row) for row in zip(*matrix)][::-1]
    return x

def extract_columns(line, widths):
    columns = []
    index = 0
    for width in widths:
        columns.append(line[index:index+width])
        index += width + 1
    return columns

def part2(lines):
    p1, operators = parse(lines)
    widths = [len(str(max(p1[i]))) for i in range(len(p1))]
    p2 = [extract_columns(l, widths) for l in lines[:-1]]
    print(len(p2), 'rows of data')
    p3 = []
    for i in range(len(widths)):
        column = []
        for j in range(len(p2)):
            column.append(p2[j][i])
        p3.append(column)
    for c in p3:
        if len(c) != 4:
            print('wrong number of rows in', c)
    total = 0
    for i in range(len(p3)):
        rotated = rotate_matrix(p3[i])
        numbers = [int(i) for i in rotated]
        print('original matrix:')
        print('\n'.join(p3[i]))
        print('rotated matrix:')
        print('\n'.join(rotated))
        print('numbers:', numbers)
        print('operator:', operators[i])

        if operators[i] == '+':
            sum = functools.reduce(operator.add, numbers)
        else:
            sum = functools.reduce(operator.mul, numbers)
        total += sum
        print('result for column', i, ':', sum, ', running total:', total)
    return total

from math import prod
def b(rows: list[str]):
    operators: list[str] = rows.pop()
    ans = 0
    values = []
    for col in reversed(range(len(operators))):
        val = ""
        for row in rows:
            digit = row[col]
            val += "" if digit == " " else digit
        if val == "":
            values = []
            continue
        values.append(int(val))
        if operators[col] == " ":
            pass
        elif operators[col] == "+":
            ans += sum(values)
            continue
        else:
            ans += prod(values)
    print(f"\nAns: {ans}")

result = part1(test_input.strip().splitlines())
assert result == 4277556, f"expected 4277556, got {result}"

result = part1(utils.read_input('day_06.txt'))
print('Part 1 -', result)

result = part2(test_input.strip().splitlines())
assert result == 3263827, f"expected 32638272, got {result}"

result = part2(utils.read_input('day_06.txt'))
print('Part 2 -', result)

result = b(utils.read_input('day_06.txt'))
print('Part 2 -', result)