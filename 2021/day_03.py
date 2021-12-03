#!/usr/bin/env python3

import utils

lines = [line.strip() for line in utils.read_input('day_03.txt')]
counts = [0 for i in range(len(lines[0]))]

for line in lines:
    for i in range(len(line)):
        if line[i] == '1':
            counts[i] += 1

gamma_counts   = ['1' if count / len(lines) >= 0.5 else '0' for count in counts]
epsilon_counts = ['1' if count / len(lines) < 0.5 else '0' for count in counts]

gamma   = int(''.join(gamma_counts), 2)
epsilon = int(''.join(epsilon_counts), 2)

power_consumption = gamma * epsilon

print('part 1 -', 'gamma:', gamma, 'epsilon:', epsilon, 'power_consumption:', power_consumption)

def most_common(digit, values):
    count_of_ones = sum([int(value[digit]) for value in values])
    if count_of_ones >= len(values) / 2:
        return '1'
    else:
        return '0'

def least_common(digit, values):
    if most_common(digit, values) == '0':
        return '1'
    else:
        return '0'

def find_rating(common_f):
    r = 0
    ratings = lines
    for i in range(len(counts)):
        d = common_f(i, ratings)
        ratings = list(filter(lambda r: r[i] == d, ratings))
        if len(ratings) == 1:
            r = int(ratings[0], 2)
            break
    return r
    
o2  = find_rating(most_common)
co2 = find_rating(least_common)
life_support_rating = o2 * co2

print('part 2 -', 'o2:', o2, 'co2:', co2, 'life_support_rating:', life_support_rating)