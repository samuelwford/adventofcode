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

priorities = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1_answer(i):
	halves = [(j[:len(j)//2], j[len(j)//2:]) for j in i]
	dupes = [list(set(a).intersection(b))[0] for a, b in halves]
	scores = [priorities.index(j) for j in dupes]
	answer = sum(scores)
	return answer
	
def p2_answer(i):
	groups = chunked(i, 3)
	badges = [list(set(a) & set(b) & set(c))[0] for a,b,c in groups]
	scores = [priorities.index(j) for j in badges]
	answer = sum(scores)
	return answer 
	
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
