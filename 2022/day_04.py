import os.path
from more_itertools import chunked

def read_input_file(fn):
	return [l.rstrip() for l in open('inputs/' + fn).readlines()]

def day():
	day, _ = os.path.splitext(os.path.basename(__file__))
	return day

def read_test_input():
	fn = day() + '_test.txt'
	return read_input_file(fn)

def read_input():
	fn = day() + '.txt'
	return read_input_file(fn)

def p1_answer(i):
	def parse_range(s):
		a, b = s.split('-')
		i, j = int(a), int(b)
		return range(i, j)
	def range_contains(a, b):
		return a.start <= b.start and a.stop >= b.stop
	def overlap(a,b):
		return range_contains(a,b) or range_contains(b,a)
	pairs = [j.split(',') for j in i]
	ranges = [(parse_range(a), parse_range(b)) for a, b in pairs]
	overlaps = filter(lambda x: overlap(x[0], x[1]), ranges)
	return len(list(overlaps))
	
def p2_answer(i):
	def parse_range(s):
		a, b = s.split('-')
		i, j = int(a), int(b)
		return range(i, j)
	def intersect(a, b):
		return (b.start >= a.start and b.start <= a.stop) or \
		       (b.stop >= a.start and b.stop <= a.stop) or \
		       (a.start >= b.start and a.start <= b.stop) or \
		       (a.stop >= b.start and a.stop <= b.stop)
	pairs = [j.split(',') for j in i]
	ranges = [(parse_range(a), parse_range(b)) for a, b in pairs]
	intersects = filter(lambda x: intersect(x[0], x[1]), ranges)
	return len(list(intersects))
		
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
