import os
import utils

class Today(utils.Day):
	def __init__(self):
		day = os.path.splitext(os.path.basename(__file__))[0]
		super().__init__(day)
		
	def parse(self, data):
		split = data.index('')
		rules = [[int(y) for y in x.split('|')] for x in data[:split]]
		pages = [[int(y) for y in x.split(',')] for x in data[split+1:]]
		return (rules, pages)
		
	def isCorrectOrder(self, set, rules):
		for p1, p2 in rules:
			if p1 in set and p2 in set and set.index(p1) > set.index(p2):
				return False
		return True
	
	def order(self, set, rules):
		applicable = [[p1, p2] for p1, p2 in rules if p1 in set and p2 in set]
		while not self.isCorrectOrder(set, rules):
			for p1, p2 in applicable:
				i1 = set.index(p1)
				i2 = set.index(p2)
				if i1 > i2:
					set[i1], set[i2] = set[i2], set[i1]
		return set
		
	def part1_answer(self, data):
		rules, pages = data
		correct = [set for set in pages if self.isCorrectOrder(set, rules)]
		answer = sum(set[len(set)//2] for set in correct)
		return answer
		
	def part2_answer(self, data):
		rules, pages = data
		incorrect = [set for set in pages if not self.isCorrectOrder(set, rules)]
		fixed = [self.order(set, rules) for set in incorrect]
		answer = sum(set[len(set)//2] for set in fixed)
		return answer
