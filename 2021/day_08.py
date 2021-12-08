#!/usr/bin/env python3

import utils

lines = [i.rstrip().split(' | ') for i in utils.read_input('day_08.txt')]
output = []

for signal, display in lines:
    output.append([signal.split(' '), display.split(' ')])

digits = {2:0,3:0,4:0,5:0,6:0,7:0}
for signal, display in output:
    for i in display:
        digits[len(i)] += 1

sum = digits[2] + digits[3] + digits[4] + digits[7]

print('part 1 - total:', sum)

# 0 =     6
# 1 = 2
# 2 =    5
# 3 =    5
# 4 =   4
# 5 =    5
# 6 =     6
# 7 =  3
# 8 =      7
# 9 =     6

# A = the shared lights from 1 & 4 removed from 7
# E = 9 has 4 & 7; the difference between 8 & 9
# G = 9 removing 4 & 7
# D = 0 is the other 6 segment that includes 1; the different between 9+G & 0
# C = the last 6 segment is 6 - the difference between 0 + D & 6
# F = 1 removing C
# B = the last one remaining

# AEGDCFB

normal_digits = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

def sort_signal(signal):
    i = [c for c in signal]
    i.sort()
    return i

def union(a, b):
    a = sort_signal(a)
    b = sort_signal(b)
    c = list(set(a + b))
    c.sort()
    return ''.join(c)

def disjoint(a, b):
    a = sort_signal(a)
    b = sort_signal(b)
    c = [x for x in a if x not in b]
    return ''.join(c)

def contains(a, b):
    for c in b:
        if not c in a:
            return False
    return True
    
def find_signal_with_size(signals, size):
    for i in signals:
        if len(i) == size:
            return i
    return ''

def find_signal_containing_with_size(signals, match, size):
    for i in signals:
        if len(i) == size and contains(i, match):
            return i
    return ''
            
def decode(signals):
    segments = {}
    segments_inv = {}
    
    to_decode = [i for i in signals]
    remaining = [i for i in 'abcdefg']
    
    # find 1, 4, 7, & 8
    one = find_signal_with_size(to_decode, 2)
    to_decode.remove(one)
    
    four = find_signal_with_size(to_decode, 4)
    to_decode.remove(four)
    
    seven = find_signal_with_size(to_decode, 3)
    to_decode.remove(seven)
    
    eight = find_signal_with_size(to_decode, 7)
    to_decode.remove(eight)    

    # a == 7 - 1
    a = disjoint(seven, one)
    remaining.remove(a)
    segments[a] = 'a'
    segments_inv['a'] = a
    
    # find 9 (contains all segments from 4+7 and has 6 total)
    tmp = union(four, seven)
    nine = find_signal_containing_with_size(to_decode, tmp, 6)
    to_decode.remove(nine)
    
    # e = 8 - 9
    e = disjoint(eight, nine)
    remaining.remove(e)
    segments[e] = 'e'
    segments_inv['e'] = e
    
    # g = 9 - (4 + 7)
    tmp = union(four, seven)
    g = disjoint(nine, tmp)
    remaining.remove(g)
    segments[g] = 'g'
    segments_inv['g'] = g
    
    # find 0 (contains 1 and has 6 total)
    zero = find_signal_containing_with_size(to_decode, one, 6)
    to_decode.remove(zero)
    
    # d = 8 - 0
    d = disjoint(eight, zero)
    remaining.remove(d)
    segments[d] = 'd'
    segments_inv['d'] = d
    
    # 6 should be the last digit with 6 segments
    six = find_signal_with_size(to_decode, 6)
    to_decode.remove(six)
    
    # c = 0 + d - 6
    c = disjoint(union(zero, segments_inv['d']), six)
    remaining.remove(c)
    segments[c] = 'c'
    segments_inv['c'] = c
    
    # f = 1 - c
    f = disjoint(one, segments_inv['c'])
    remaining.remove(f)
    segments[f] = 'f'
    segments_inv['f'] = f
    
    # b = last remaining segment
    b = remaining[0]
    remaining.remove(b)
    segments[b] = 'b'
    segments_inv['b'] = b
    
    decoded = {}
    for signal in normal_digits.keys():
        scrambled = [segments_inv[c] for c in signal]
        scrambled.sort()
        scrambled = ''.join(scrambled)
        decoded[scrambled] = normal_digits[signal]
    
    return decoded

def decode_digit(map, code):
    a = sort_signal(code)
    a = ''.join(a)
    return map[a]

total = 0
for signals, digits in output:
    decoded = decode(signals)
    reading = int(''.join([decode_digit(decoded, digit) for digit in digits]))
    total += reading

print('part 2 - sum of outputs', total)