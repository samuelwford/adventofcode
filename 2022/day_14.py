import os.path
import numpy

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

def parse_input(i):
	lines = []
	for j in i:
		line = []
		for c in j.split(' -> '):
			x, y = c.split(',')
			line.append((int(x), int(y)))
		lines.append(line)
	return lines

def measure_cave(lines):
	minx, maxx, maxy = 500, 500, 0
	for line in lines:
		for x, y in line:
			if x < minx: minx = x
			if x > maxx: maxx = x
			if y > maxy: maxy = y
	return (minx, maxx, maxy)

def print_cave(cave):
	for row in cave:
		print(''.join(row))
		
def create_cave(lines):
	minx, maxx, maxy = measure_cave(lines)
	w, h = maxx - minx + 1, maxy + 1	
	cave = []
	for _ in range(h):
		row = []
		for _ in range(w):
			row.append('.')
		cave.append(row)
	
	def draw(p1, p2):
		x1, y1 = p1
		x2, y2 = p2
		x1 -= minx
		x2 -= minx
		
		dx = numpy.sign(x2 - x1)
		dy = numpy.sign(y2 - y1)
		
		x, y = x1, y1
		cave[y][x] = '#'
		while True:
			x += dx
			y += dy
			cave[y][x] = '#'
			if x == x2 and y == y2:
				break
			
	for line in lines:
		for p1, p2 in zip(line[:(len(line) - 1)], line[-(len(line) - 1):]):
			draw(p1, p2)
	
	return (minx, cave)

def drop_sand(minx, cave):
	x, y, w, h = 500 - minx, 0, len(cave[0]), len(cave)
	while cave[y][x] == '.':
		if y == len(cave) - 1:
			print('off the bottom', y)
			return False
		if cave[y + 1][x] == '.':
			y += 1
		elif x == 0:
			print('off the left', x)
			return False
		elif cave[y + 1][x - 1] == '.':
			y += 1
			x -= 1
		elif x == len(cave[0]):
			print('off the right', x)
			return False
		elif cave[y + 1][x + 1] == '.':
			y += 1
			x += 1
		else:
			cave[y][x] = 'o'
			return True
	
def p1_answer(i):
	lines = parse_input(i)
	minx, cave = create_cave(lines)
	
	s = 0
	while drop_sand(minx, cave):
		s += 1
	
	return s
		
def p2_answer(i):
	lines = parse_input(i)
	minx, cave = create_cave(lines)
	
	h = len(cave) + 1
	w = (h * 2) -1
	
	lines.append([(500 - w // 2 - 2, h), (500 + w // 2 + 2, h)])
	minx, cave = create_cave(lines)
	
	s = 0
	while drop_sand(minx, cave):
		s += 1
	
	print_cave(cave)
		
	return s

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
