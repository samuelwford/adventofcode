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

def parse(i):
	pairs = []
	while len(i) > 0:
		lh = eval(i.pop(0))
		rh = eval(i.pop(0))
		if len(i) > 0:
			i.pop(0)
		pairs.append((lh, rh))
	return pairs

def parse2(i):
	return [eval(j) for j in i if len(j) > 0]

def compare(lh, rh):
	if isinstance(lh, int) and isinstance(rh, int):
		if lh < rh:
			return -1
		if lh == rh:
			return 0
		if lh > rh:
			return 1
	
	if not isinstance(lh, list):
		lh = [lh]
		
	if not isinstance(rh, list):
		rh = [rh]
		
	for i in range(len(lh)):
		if i > len(rh) - 1:
			return 1
		
		order = compare(lh[i], rh[i])
		
		if order == -1 or order == 1:
			return order
		
	return -1
	
def p1_answer(i):
	pairs = parse(i)
	idxs = []
	for idx in range(len(pairs)):
		lh, rh = pairs[idx]
		if compare(lh, rh) == -1:
			idxs.append(idx + 1)
	return sum(idxs)

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def p2_answer(i):
	packets = parse2(i)
	packets.append([[2]])
	packets.append([[6]])
	ordered = sorted(packets, key = cmp_to_key(compare))
	d1 = ordered.index([[2]]) + 1
	d2 = ordered.index([[6]]) + 1
	return d1 * d2

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
