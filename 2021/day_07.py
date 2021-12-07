#!/usr/bin/env python3

import utils

#crabs = [16,1,2,0,4,2,7,1,2,14]
crabs = [int(i) for i in utils.read_input('day_07.txt')[0].split(',')]

med_s = len(crabs) // 2
med_e = med_s + (len(crabs) + 1) % 2

s = sorted(crabs)

best_s = s[med_s]
best_s = sum(abs(x - best_s) for x in crabs)

best_e = s[med_e]
best_e = sum(abs(x - best_e) for x in crabs)

best = min(best_s, best_e)

print('part 1 - position:', best)

pos = sum(crabs) // len(crabs)
fuel_1 = sum(abs(x - pos) * (abs(x - pos) + 1) // 2 for x in crabs)
fuel_2 = sum(abs(x - (pos + 1)) * (abs(x - (pos + 1)) + 1) // 2 for x in crabs)

fuel = min(fuel_1, fuel_2)

print('part 2 - fuel:', fuel)