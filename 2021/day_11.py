import copy

# sample input
# input = [
#     "5483143223",
#     "2745854711",
#     "5264556173",
#     "6141336146",
#     "6357385478",
#     "4167524645",
#     "2176841721",
#     "6882881134",
#     "4846848554",
#     "5283751526"
# ]

# puzzle input
input = [
    "3322874652",
    "5636588857",
    "7755117548",
    "5854121833",
    "2856682477",
    "3124873812",
    "1541372254",
    "8634383236",
    "2424323348",
    "2265635842",    
]

octo = [[int(c) for c in r] for r in input]

def in_grid(g, x, y):
    return y > -1 and y < len(g) and x > -1 and x < len(g[y])
    
def flash(g, f, x, y):
    if f[y][x]:
        return
    if g[y][x] < 10:
        return
    f[y][x] = True
    for dx, dy in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]:
        x1 = x + dx
        y1 = y + dy
        if in_grid(g, x1, y1) and not f[y1][x1]:
            g[y + dy][x + dx] += 1
            flash(g, f, x1, y1)
    
def cycle(g):
    f = [[False for x in y] for y in g]
    for y in range(len(g)):
        for x in range(len(g[y])):
            g[y][x] += 1
    for y in range(len(g)):
        for x in range(len(g[y])):
            flash(g, f, x, y)
    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x] > 9:
                g[y][x] = 0
    flashes = sum(sum(1 if c else 0 for c in r) for r in f)
    return flashes

total = 0
for c in range(100):
    flashes = cycle(octo)
    total += flashes

print('part 1 - flashes after 100 cycles', total)

octo = [[int(c) for c in r] for r in input]
gen = 0
while True:
    gen += 1
    flashes = cycle(octo)
    if flashes == 100:
        break

print('part 2 - synchronization at cycle', gen)