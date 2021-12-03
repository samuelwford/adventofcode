#!/usr/bin/env python3

import utils

lines = [line.strip() for line in utils.read_input('day_03.txt')]
counts = [0 for i in range(len(lines[0]))]

for line in lines:
    for i in range(len(line)):
        if line[i] == '1':
            counts[i] += 1

gamma_counts   = [1 if count / len(lines) >= 0.5 else 0 for count in counts]
epsilon_counts = [1 if count / len(lines) < 0.5 else 0 for count in counts]

bits = [2**i for i in range(len(counts))]
bits = bits[::-1]

gamma_bits = [a * b for (a, b) in zip(gamma_counts, bits)]
gamma      = sum(gamma_bits)

epsilon_bits = [a * b for (a, b) in zip(epsilon_counts, bits)]
epsilon      = sum(epsilon_bits)

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

o2_str = ''
o2 = 0
ratings = lines
for i in range(len(counts)):
    d = most_common(i, ratings)
    ratings = list(filter(lambda r: r[i] == d, ratings))
    if len(ratings) == 1:
        o2_str = ratings[0]
        o2 = int(o2_str, 2)
        break

co2_str = ''
co2 = 0
ratings = lines
for i in range(len(counts)):
    d = least_common(i, ratings)
    ratings = list(filter(lambda r: r[i] == d, ratings))
    if len(ratings) == 1:
        co2_str = ratings[0]
        co2 = int(co2_str, 2)
        break

life_support_rating = o2 * co2

print('part 2 -', 'o2:', o2_str, o2, 'co2:', co2_str, co2, 'life_support_rating:', life_support_rating)