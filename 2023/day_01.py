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

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def p2_parse(i):
	def get_calibration_value(line):
		reversed_line = line[::-1]
		start = -1
		end = -1
		current = 0
		while start < 0 or end < 0: #current < len(line):
			if start < 0:
				if line[current].isdigit():
					start = int(line[current])
				else:
					for key, value in enumerate(numbers):
						if line[current:current+len(value)] == value:
							start = key
							break
			if end < 0:
				if reversed_line[current].isdigit():
					end = int(reversed_line[current])
				else:
					for key, value in enumerate(numbers):
						reversed_value = value[::-1]
						if reversed_line[current:current+len(reversed_value)] == reversed_value:
							end = key
							break
			current = current + 1
		return int(str(start) + str(end))
					
	return [get_calibration_value(j) for j in i]

def p1_parse(i):
	def get_calibration_value(line):
		reversed_line = line[::-1]
		start = -1
		end = -1
		current = 0
		while start < 0 or end < 0: #current < len(line):
			if start < 0:
				if line[current].isdigit():
					start = int(line[current])
			if end < 0:
				if reversed_line[current].isdigit():
					end = int(reversed_line[current])
			current = current + 1
		return int(str(start) + str(end))
					
	return [get_calibration_value(j) for j in i]
	  
def p1_answer(i):
	digits = p1_parse(i)
	return sum(digits)
	
def p2_answer(i):
	digits = p2_parse(i)
	return sum(digits)
	
def p1():
	a = p1_answer(read_test_input())
	print('part 1 test:', a)
	
	a = p1_answer(read_input())
	print('part 1:', a)

def p2():
	a = p2_answer(read_test_input('2'))
	print('part 2 test:', a)
	
	a = p2_answer(read_input())
	print('part 2:', a)

p1()
p2()
