import utils

class Today(utils.Day):
	def parse(self, data):
		nms = [[int(y) for y in x.split("   ")] for x in data]
		n1 = sorted([x for x, y in nms])
		n2 = sorted([y for x, y in nms])
		n = list(zip(n1, n2))
		return n
		
	def part1_answer(self, data):
		diffs = [abs(x - y) for x, y in data]
		print(diffs)
		return sum(diffs)
		
Today().run()
