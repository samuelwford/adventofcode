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
	root = {}
	cwd = {}
	for j in i:
		if j == '$ cd ..':
			cwd = cwd['..']
		elif j.startswith('$ cd '):
			n = j[5:]
			if 'dirs' in cwd:
				cwd = cwd['dirs'][n]	
			else:
				cwd = {'name': n, 'dirs': {}, 'files': []}
				root = cwd
		elif j == '$ ls':
			pass
		elif j.startswith('dir '):
			n = j[4:]
			nd = {'..': cwd, 'name': n, 'dirs': {}, 'files': []}
			cwd['dirs'][n] = nd
		else:
			s, n = j.split()
			cwd['files'].append((int(s), n))
	return root

def compute_sizes(d):
	s = 0
	for f in d['files']:
		s += f[0]
	for sd in d['dirs']:
		s += compute_sizes(d['dirs'][sd])
	d['size'] = s
	return s
	
def find_p1_sizes(d):
	s = []
	ds = d['size']
	if ds <= 100000:
		s.append(ds)
	for sd in d['dirs']:
		s.extend(find_p1_sizes(d['dirs'][sd]))
	return s

def find_p2_sizes(d, sz):
	s = []
	ds = d['size']
	if ds >= sz:
		s.append(ds)
	for sd in d['dirs']:
		s.extend(find_p2_sizes(d['dirs'][sd], sz))
	return s
	
def p1_answer(i):
	tree = parse_input(i)
	size = compute_sizes(tree)
	sizes = find_p1_sizes(tree)
	return sum(sizes)
	
def p2_answer(i):
	tree = parse_input(i)
	size = compute_sizes(tree)
	free_space = 70000000 - tree['size']
	needed = 30000000 - free_space
	sizes = find_p2_sizes(tree, needed)
	return min(sizes)
		
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
