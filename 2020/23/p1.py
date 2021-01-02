##!/usr/bin/env python

input = [6,2,4,3,9,7,1,5,8]

def cycle(cups, current):
    label = cups[current]
    next_label = label - 1
    
    print("cups:", end=" ")
    for i in range(0,len(cups)):
        if i == current:
            print(f"({cups[i]})", end=" ")
        else:
            print(cups[i], end=" ")
    print()

    head = [cups.pop((current + 1) % len(cups)), cups.pop((current + 1) % len(cups)), cups.pop((current + 1) % len(cups))]
    while not next_label in cups:
        next_label -= 1
        if next_label == 0: next_label = 9
    destination = cups.index(next_label)
    
    print("pick up:", head)
    print("destination:", next_label)
    print(" -- before insert:", cups)
    print(" -- insert at index:", destination)

    cups[destination + 1:destination + 1] = head
    current = (current + 9) % 9 + 1

    return (cups, current)

print("-- move 1 --")
list, i = cycle([3,8,9,1,2,5,4,6,7], 0)

print("-- move 2 --")
list, i = cycle(list, i)

print("-- move 3 --")
list, i = cycle(list, i)

print("-- move 4 --")
list, i = cycle(list, i)

print("-- move 5 --")
list, i = cycle(list, i)

print("-- move 6 --")
list, i = cycle(list, i)
