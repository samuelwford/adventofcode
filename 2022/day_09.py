import os.path

def read_input_file(fn):
	return [l.rstrip('\n') for l in open('inputs/' + fn).readlines()]

def day():
	day, _ = os.path.splitext(os.path.basename(__file__))
	return day

def read_test_input():
	fn = day() + '_test.txt'
	return read_input_file(fn)

def read_test_input2():
	fn = day() + '_test2.txt'
	return read_input_file(fn)

def read_input():
	fn = day() + '.txt'
	return read_input_file(fn)

def parse_input(i):
	return [(a, int(b)) for a, b in [j.split() for j in i]]

def move_rope(moves):
	hx, hy, tx, ty = 0, 0, 0, 0
	
	p = [(tx, ty)]
	m = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
	
	for direction, steps in moves:
		for _ in range(steps):
			mx, my = m[direction]
			px, py = hx, hy
			hx += mx
			hy += my
			if abs(hx - tx) > 1 or abs(hy - ty) > 1:
				tx, ty = px, py
				p.append((tx, ty))
	
	return p
	
def move_long_rope(moves):
	v = [(0, 0)]
	m = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
	
	rope = []
	for _ in range(10):
		rope.append((0, 0))
	
	for direction, steps in moves:
		for _ in range(steps):
			mx, my = m[direction]
			for i in range(len(rope) - 1):
				hx, hy = rope[i]
				tx, ty = rope[i + 1]
				px, py = hx, hy
				
				hx += mx
				hy += my
				rope[i] = (hx, hy)
				
				if abs(hx - tx) > 1 or abs(hy - ty) > 1:
					rope[i + 1] = (px, py)
					mx, my = px - tx, py - ty
					if i + 1 == 9:
						v.append((px, py))
				else:
					break
	
	return v
		
def p1_answer(i):
	return len(set(move_rope(parse_input(i))))
	
def p2_answer(i):
	return len(set(move_long_rope(parse_input(i))))
		
def p1():
	a = p1_answer(read_test_input())
	print('part 1 test:', a)
	
	a = p1_answer(read_input())
	print('part 1:', a)

def p2():
	a = p2_answer(read_test_input())
	print('part 2 test:', a)
	
	a = p2_answer(read_test_input2())
	print('part 2 test 2:', a)
	
	#a = p2_answer(read_input())
	#print('part 2:', a)

p1()
p2()
