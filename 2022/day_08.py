import os.path

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
	a = []
	for j in i:
		a.append([int(k) for k in j])
	return a

def	is_visible(f, x, y):
	h, w = len(f), len(f[0])
	vt, vb, vl, vr = True, True, True, True
	t = f[y][x]
	for i in range(x - 1, -1, -1):
		if f[y][i] >= t:
			vl = False
	for i in range(x + 1, w):
		if f[y][i] >= t:
			vr = False
	for i in range(y - 1, -1, -1):
		if f[i][x] >= t:
			vt = False
	for i in range(y + 1, h):
		if f[i][x] >= t:
			vb = False
	return vl or vr or vt or vb

def	number_visible(f, x, y):
	h, w = len(f), len(f[0])
	vt, vb, vl, vr = 0, 0, 0, 0
	t = f[y][x]
	
	for i in range(x - 1, -1, -1):
		vl += 1
		if f[y][i] >= t:
			break
	
	for i in range(x + 1, w):
		vr += 1
		if f[y][i] >= t:
			break
	
	for i in range(y - 1, -1, -1):
		vt += 1
		if f[i][x] >= t:
			break
			
	for i in range(y + 1, h):
		vb += 1
		if f[i][x] >= t:
			break
			
	return vl * vr * vt * vb
		
def p1_answer(i):
	f = parse_input(i)
	h, w = len(f), len(f[0])
	v = 0
	for x in range(w):
		for y in range(h):
			if is_visible(f, x, y):
				v += 1
	return v
	
def p2_answer(i):
	f = parse_input(i)
	h, w = len(f), len(f[0])
	m = 0
	for x in range(w):
		for y in range(h):
			v = number_visible(f, x, y)
			if v > m:
				m = v	
	return m
		
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
