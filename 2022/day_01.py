import os.path
from more_itertools import split_at

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

def compute(i):
	sets = list(split_at(i, lambda x: x == ''))
	sums = sorted([sum([int(i) for i in s]) for s in sets])
	return sums
  
def p1_answer(i):
	d = compute(i)
	return d[-1]
	
def p2_answer(i):
	d = compute(i)
	return sum(d[-3:])
	
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
