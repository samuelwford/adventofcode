import os.path
import re

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
	stacks = []
	moves = []
	
	print(range((len(i[0]) + 1) // 4))
	for j in range((len(i[0]) + 1) // 4):
		stacks.append([])
	
	def parse_stack(s):
		for j in range((len(s) + 1) // 4):
			k = s[j * 4 + 1]
			if k != ' ' and not k.isnumeric():
				stacks[j].append(k)
				
	def parse_move(m):
		j = m.split(' ')
		moves.append((int(j[1]), int(j[3]), int(j[5])))
		
	k = False
	for j in i:
		if j == '':
			k = True
			continue
		if k:
			parse_move(j)
		else:
			parse_stack(j)
	
	return (stacks, moves)
	
def p1_answer(i):
	stacks, moves = parse_input(i)
	def execute(move):
		boxes, from_stack, to_stack = move
		for i in range(boxes):
			box = stacks[from_stack - 1].pop(0)
			stacks[to_stack - 1].insert(0, box)
	
	for move in moves:
		execute(move)
	
	top_boxes = ''.join([s[0] for s in stacks])
	return top_boxes
	
def p2_answer(i):
	stacks, moves = parse_input(i)
	def execute(move):
		boxes, from_stack, to_stack = move
		temp = []
		for i in range(boxes):
			box = stacks[from_stack - 1].pop(0)
			temp.insert(0, box)
		for i in range(len(temp)):
			box = temp.pop(0)
			stacks[to_stack - 1].insert(0, box)
	
	for move in moves:
		execute(move)
	
	top_boxes = ''.join([s[0] for s in stacks])
	return top_boxes
		
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
