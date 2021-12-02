#!/usr/bin/env python3

import utils

cmds = [line.split(' ') for line in utils.read_input('day_02.txt')]
cmds = [(a, int(b)) for (a, b) in cmds]

horiz = 0
depth = 0

horiz = sum([b for (a, b) in cmds if a == 'forward'])
down  = sum([b for (a, b) in cmds if a == 'down'])
up    = sum([b for (a, b) in cmds if a == 'up'])
depth = down - up
pos   = horiz * depth

print('part 1 - horiz:', horiz, 'depth:', depth, 'pos:', pos)

horiz = 0
depth = 0
aim   = 0

for (a, b) in cmds:
    if a == 'forward':
        horiz += b
        depth += b * aim

    if a == 'down':
        aim += b
    
    if a == 'up':
        aim -= b

pos = horiz * depth

print('part 2 - horiz:', horiz, 'aim:', aim, 'depth:', depth, 'pos:', pos)