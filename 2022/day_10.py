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
		
def compute(i):
	clk = 0
	a = 1
	wc = 0
	s = []
	r = ''
	while len(i) > 0:
		clk += 1
		if wc == 0:
			j = i.pop(0)
			if j[:4] == 'addx':
				wc = 1
		else:
			wc -= 1
		
		if wc == 0 and j[:4] == 'addx':
			k = int(j[5:])
			a += k
			
		if (clk + 20) % 40 == 0:
			s.append(a * clk)
		
		b = clk % 40 + 1
		if b >= a and b <= (a + 2):
			r += "#"
		else:
			r += '.'
	
	return (sum(s), r)

def p1_answer(i):
	a, _ = compute(i)
	return a
		
def p2_answer(i):
	_, a = compute(i)
	return a

def print_display(i):
	for j in range(0,len(i), 40):
		print(i[j:j+40])
	
def p1():
	a = p1_answer(read_test_input())
	print('part 1 test:', a)
	
	a = p1_answer(read_input())
	print('part 1:', a)

def p2():
	a = p2_answer(read_test_input())
	print('part 2 test:')
	print_display(a)
	
	a = p2_answer(read_input())
	print('part 2:')
	print_display(a)

p1()
p2()
