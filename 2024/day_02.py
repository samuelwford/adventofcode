import utils
from functools import reduce

class Today(utils.Day):
	def __init__(self):
		super().__init__("day_02")
		
	def parse(self, data):
		reports = [[int(y) for y in x.split()] for x in data]
		return reports
		
	def isSafe(self, report):
		a = [x-y for x,y in zip(report[:-1], report[1:])]
		b1 = all(x < 0 for x in a)
		b2 = all(x > 0 for x in a)
		c = all(abs(x)>0 and abs(x)<4 for x in a)
		d = (b1 or b2) and c
		return 1 if d else 0
	
	def isSafeWithDampener(self, report):
		if self.isSafe(report):
			return 1
		
		for i in range(len(report)):
			tmp = report[:]
			del tmp[i]
			if self.isSafe(tmp):
				return 1
		
		return 0
		
	def part1_answer(self, data):
		safe = reduce(lambda count, i: count + self.isSafe(i), data, 0)
		return safe
		
	def part2_answer(self, data):
		safe = reduce(lambda count, i: count + self.isSafeWithDampener(i), data, 0)
		return safe