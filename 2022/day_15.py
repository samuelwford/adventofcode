import os.path
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

def parse_input(i):
	def parse_line(s):
		s = s[12:]
		c = s.index(',')
		x1 = int(s[:c])
		s = s[4 + c:]
		c = s.index(':')
		y1 = int(s[:c])
		s = s[25 + c:]
		c = s.index(',')
		x2 = int(s[:c])
		s = s[4 + c:]
		y2 = int(s)
		return (x1, y1, x2, y2)
	
	return [parse_line(j) for j in i]

def distance(x1, y1, x2, y2):
	return abs(x2 - x1) + abs(y2 - y1)

def p1_answer(i, row):
	coords = parse_input(i)
	minx, maxx, miny, maxy = inf, -inf, inf, -inf
	for x1, y1, x2, y2 in coords:
		r = distance(x1, y1, x2, y2)
		if x1 - r < minx: minx = x1
		if x1 + r > maxx: maxx = x1
		if y1 - r < miny: miny = y1
		if y1 + r > maxy: maxy = y1
	
	print(minx, miny, maxx, maxy)
	
	missing = 0
	q = ''
	for x in range(minx, maxx):
		d = '.'
		for x1, y1, x2, y2 in coords:
			d1, d2 = distance(x, row, x1, y1), distance(x1, y1, x2, y2)
			if d1 <= d2:
				print(x, 'is', d1, 'from sensor, inside the radius', d2, 'of', x1, y1, x2, y2)
				missing += 1
				d = '#'
				break
		q += d
		
	print(q)
	
	return missing
		
def p2_answer(i):
	return 0

def p1():
	a = p1_answer(read_test_input(), 10)
	print('part 1 test:', a)
	
	#a = p1_answer(read_input(), 2000000)
	#print('part 1:', a)

def p2():
	a = p2_answer(read_test_input())
	print('part 2 test:', a)
	
	a = p2_answer(read_input())
	print('part 2:', a)

p1()
p2()
