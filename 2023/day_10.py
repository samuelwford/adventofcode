import utils

class Today(utils.Day):
    def parse(self, data):
        return super().parse(data)
    
    def find_start(grid):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 'S':
                    return (x, y)
        return (0,0)
    
    exits = {'S': 'NSEW', '-': 'EW', '|': 'NS', 'L': 'NE', '7': 'SW', 'J': 'NW', 'F': 'SE', '.': ''}
    connections = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}

    def find_exits(grid, l):
        x, y = l
        p = grid[y][x]
        e = Today.exits[p]
        el = []
        for cd in e:
            dx, dy = Today.directions[cd]
            nx, ny = x, y
            if x + dx >= 0 and x + dx < len(grid[y]):
                nx = x + dx
            if y + dy >= 0 and y + dy < len(grid):
                ny = y + dy
            if nx != x and ny != y:
                el.append((cd, nx, ny))
        return el

    def part1_answer(self, data):
        start = Today.find_start(data)
        el1 = Today.find_exits(data, start)
        for d, x, y in el1:
            el2 = Today.find_exits(data, (x, y))
            for d2, x2, y2 in el2:
                if x == x2 and y == y2:
                    continue
                if Today.directions[d] == d2:
                    
                
        return super().part1_answer(data)
    
    def part2_answer(self, data):
        return super().part2_answer(data)
    
Today().run()