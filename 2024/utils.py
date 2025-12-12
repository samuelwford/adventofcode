import os.path
import inspect

class Day:
	def __init__(self, day):
		self.day = day
		self.test_data = self.read_test_data()
		self.test_data2 = self.read_test_data('2')
		self.data = self.read_data()
		
	def read_data_file(self, fn):
		if os.path.exists('inputs/' + fn):
			return [l.rstrip() for l in open('inputs/' + fn).readlines()]
		else:
			print('Data File Doesn\'t Exist', fn)
			return []

	def read_test_data(self, suffix=''):
		fn = self.day + '_test' + suffix + '.txt'
		if not os.path.exists('inputs/' + fn):
			fn = self.day + '_test.txt'
		return self.read_data_file(fn)
		
	def read_data(self):
		fn = self.day + '.txt'
		return self.read_data_file(fn)
	
	def parse(self, data):
		return data
	
	def part1_parse(self, data):
		return self.parse(data)
	
	def part2_parse(self, data):
		return self.parse(data)
		
	def part1_answer(self, data):
		return len(self.data)
		
	def part2_answer(self, data):
		return len(self.data)
	
	def part1(self):
		parsed_data = self.part1_parse(self.test_data)
		answer = self.part1_answer(parsed_data)
		print('Part 1 Test:', answer)
		
		parsed_data = self.part1_parse(self.data)
		answer = self.part1_answer(parsed_data)
		print('Part 1:', answer)
				
	def part2(self):
		parsed_data = self.part2_parse(self.test_data2)
		answer = self.part2_answer(parsed_data)
		print('Part 2 Test:', answer)
		
		parsed_data = self.part2_parse(self.data)
		answer = self.part2_answer(parsed_data)
		print('Part 2:', answer)
				
	def run(self):
		print('Running', self.day)
		self.part1()
		self.part2()

