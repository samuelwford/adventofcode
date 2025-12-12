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
    moves = [m.split(' ') for m in i]
    return moves
    
def eval_turn_p1(a, b):
    if a == 'A':
        if b == 'X':
            return 1 + 3
        elif b == 'Y':
            return 2 + 6
        else:
            return 3 + 0
    elif a == 'B':
        if b == 'X':
            return 1 + 0
        elif b == 'Y':
            return 2 + 3
        else:
            return 3 + 6
    else:
        if b == 'X':
            return 1 + 6
        elif b == 'Y':
            return 2 + 0
        else:
            return 3 + 3            

def eval_turn_p2(a, b):
    # a, b, c = rock, paper, scissors
    # x = lose, y = draw, z = win
    if a == 'A': # rock (paper win, scissors lose)
        if b == 'X': # lose with scissors
            return 3 + 0
        elif b == 'Y': # draw with rock
            return 1 + 3
        else: # win with paper
            return 2 + 6
    elif a == 'B': # paper (scissors win, rock lose)
        if b == 'X': # lose with rock
            return 1 + 0
        elif b == 'Y': # draw with paper
            return 2 + 3
        else: # win with scissors
            return 3 + 6
    else: # scissors (rock win, paper lose)
        if b == 'X': # lose with paper
            return 2 + 0
        elif b == 'Y': # draw with scissors
            return 3 + 3
        else: # win with rock
            return 1 + 6            
               
def p1_answer(i):
	m = compute(i)
	d = [eval_turn_p1(a, b) for a, b in m]
	return sum(d)
	
def p2_answer(i):
	m = compute(i)
	d = [eval_turn_p2(a, b) for a, b in m]
	return sum(d)
	
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
