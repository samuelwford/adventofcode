import utils

class Today(utils.Day):
	def parse(self, data):
		nms =[[int(y) for y in x.split()] for x in data]
		return nms
	
	def compute_diffs(seq):
		x = []
		for i in range(len(seq) - 1):
			x.append(seq[i + 1] - seq[i])
		return x

	def next_seq(seq):
		stack = [seq]
		while True:
			next = Today.compute_diffs(stack[-1])
			stack.append(next)
			if all(x == 0 for x in next):
				break
		n, m = 0, 0
		for i in range(len(stack) - 1, -1, -1):
			n = n - stack[i][0]
			m = m + stack[i][-1]
		return (n, m)
	
	def part1_answer(self, data):
		seqs = [Today.next_seq(x) for x in data]
		ends = [m for n, m in seqs]
		return sum(ends)
	
	def part2_answer(self, data):
		seqs = [Today.next_seq(x) for x in data]
		starts = [n for n, m in seqs]
		return sum(starts)

	

Today().run()
