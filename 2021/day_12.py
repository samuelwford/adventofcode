#!/usr/bin/env python3

import utils

segments = [line.split('-') for line in utils.read_input('day_12.txt')]

nodes = {}
for a, b in segments:
    if a in nodes:
        if b not in nodes[a]:
            nodes[a].append(b)
    else:
        nodes[a] = [b]
    if b in nodes:
        if a not in nodes[b]:
            nodes[b].append(a)
    else:
        nodes[b] = [a]

print(segments)
print(nodes)

def explore_from(n, p):
    for sn in nodes[n]:
        np = []
        
    
n = nodes['start']

