import os.path
#from more_itertools import split_at

def read_input_file(fn):
	return [l.rstrip() for l in open('inputs/' + fn).readlines()]

def day():
	day, _ = os.path.splitext(os.path.basename(__file__))
	return day

def read_test_input(suffix=''):
	fn = day() + '_test' + suffix + '.txt'
	return read_input_file(fn)

def read_input():
	fn = day() + '.txt'
	return read_input_file(fn)

class Game:
	def __init__(self, line):
		a, b = line.split(':')
		_, g = a.split()
		self.game = int(g)
		self.turns = []
		ts = b.split(';')
		for t in ts:
			ds = [d.strip() for d in t.split(',')]
			dm = {'red': -1, 'green': -1, 'blue': -1}
			for d in ds:
				count, color = d.split()
				dm[color] = int(count)
			self.turns.append(dm)

	def is_possible(self, r, g, b):
		x = True
		for t in self.turns:
			if t['red'] > r or t['green'] > g or t['blue'] > b:
				x = False
				break		
		return x
	
	def power(self):
		r, g, b = -1, -1, -1
		for t in self.turns:
			if t['red'] > r: r = t['red']
			if t['green'] > g: g = t['green']
			if t['blue'] > b: b = t['blue']
		return r * g * b
	
def parse(i):
	games = [Game(l) for l in i]
	return games
	  
def p1_answer(i):
	games = parse(i)
	gns = [g.game for g in games if g.is_possible(12, 13, 14)]
	return sum(gns)
	
def p2_answer(i):
	games = parse(i)
	pws = [g.power() for g in games]
	return sum(pws)
	
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
