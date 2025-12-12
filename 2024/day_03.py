import os
import re
import utils

class Today(utils.Day):
	def __init__(self):
		day = os.path.splitext(os.path.basename(__file__))[0]
		super().__init__(day)
		
	def parse(self, data):
		result = [(int(i), int(j)) for i, j in re.findall(r"mul\((\d+),(\d+)\)", '\n'.join(data))]
		return result
	
	def part2_parse(self, data):
		result = re.findall(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", '\n'.join(data))
		return result
		
	def part1_answer(self, data):
		a = sum(x * y for x, y in data)
		return a
		
	def part2_answer(self, data):
		ignore = False
		total = 0
		for x in data:
			if x[4] == "don't()":
				ignore = True
			elif x[3] == "do()":
				ignore = False
			elif not ignore:
				i = int(x[1])
				j = int(x[2])
				total = total + i * j
		return total
