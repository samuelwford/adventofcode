#!/usr/bin/env python
import os

fname = os.path.join(os.path.dirname(__file__), 'input.txt')
input = open(fname).read()
d1, d2 = input.split('\n\n')
d1, d2 = [int(i) for i in d1.splitlines()[1:]], [int(i) for i in d2.splitlines()[1:]]

r = 0
while len(d1) > 0 and len(d2) > 0:
    r += 1
    print(f"-- Round {r} --")
    print("Player 1's deck:", d1)
    print("Player 2's deck:", d2)
    c1, c2 = d1.pop(0), d2.pop(0)
    print("Player 1 plays:", c1)
    print("Player 2 plays:", c2)
    if c1 > c2:
        d1.append(c1)
        d1.append(c2)
        print("Player 1 wins the round!")
    else:
        d2.append(c2)
        d2.append(c1)
        print("Player 2 wins the round!")
    print()

d = d1 or d2
score = sum((len(d) - i) * c for i, c in enumerate(d))
print(score)