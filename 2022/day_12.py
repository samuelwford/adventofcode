import os.path
from itertools import product
from math import inf

def read_input_file(fn):
	return [l.rstrip('\n') for l in open('inputs/' + fn).readlines()]

def day():
	day, _ = os.path.splitext(os.path.basename(__file__))
	return day

def read_test_input():
	fn = day() + '_test.txt'
	return read_input_file(fn)

def read_input():
	fn = day() + '.txt'
	return read_input_file(fn)

def create_nodes(grid):
	return list(product(range(len(grid[0])), range(len(grid))))

def adjacent_to(grid, p):
	scale = 'SabcdefghijklmnopqrstuvwxyzE'
	neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	
	x, y = p
	w, h = len(grid[0]), len(grid)
	
	curr = scale.index(grid[y][x])
	adj = []
	
	for dx, dy in neighbors:
		x2, y2 = x + dx, y + dy
		if x2 >= 0 and x2 < w and y2 >= 0 and y2 < h:
			n = scale.index(grid[y2][x2])
			if n - curr < 2:
				adj.append((x2, y2))
	
	return adj
		
def dijkstra(grid, src, dest):
	q = create_nodes(grid)
	dist = {node : inf for node in q}
	prev = {node : None for node in q}
	
	dist[src] = 0
	
	while q:
		u = min(q, key = dist.__getitem__)
		q.remove(u)
		
		for v in adjacent_to(grid, u):
			alt = dist[u] + 1
			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u
				
	path = [dest]
	cur = dest
	
	while prev[cur]:
		path.append(prev[cur])
		cur = prev[cur]
		
	return list(reversed(path))

def find_src_dest(grid):
	src, dest = (0, 0), (0, 0)
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 'S':
				src = (x, y)
			if grid[y][x] == 'E':
				dest = (x, y)
	return src, dest

def find_possible_src_list(grid):
	src, dest = [], (0, 0)
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 'a':
				src.append((x, y))
			if grid[y][x] == 'E':
				dest = (x, y)
	return src, dest	
	
def p1_answer(i):
	src, dest = find_src_dest(i)
	a = dijkstra(i, src, dest)
	return len(a) - 1
		
def p2_answer(i):
	srcs, dest = find_possible_src_list(i)
	min = inf
	print('number of starts:', len(srcs))
	s = 0
	for src in srcs:
		s += 1
		a = dijkstra(i, src, dest)
		if i[a[0][1]][a[0][0]] == 'a' and len(a) < min:
			print('found:', src, 'length', len(a), 'start:', i[a[0][1]][a[0][0]])
			min = len(a)

	return min - 1

def p1():
	a = p1_answer(read_test_input())
	print('part 1 test:', a)
	
	a = p1_answer(read_input())
	print('part 1:', a)

def p2():
	a = p2_answer(read_test_input())
	print('part 2 test:', a)
	
	a = p2_answer(read_input())
	print('part 2:', a)

p1()
p2()
