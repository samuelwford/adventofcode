import utils

class PartNumber:
	def __init__(self, x, y, n):
		self.x = x
		self.y = y
		self.n = n
		
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
		
	def __repr__(self):
		return "({},{}): {}".format(self.x, self.y, self.n)

class Today(utils.Day):
	def part1_parse(self, i):
		h, w = len(i), len(i[0])
		p = []
		for x in range(w):
			for y in range(h):
				c = i[y][x]
				if c != '.' and not c.isdigit():
					# we found a symbol
					pns = self.find_numbers(i, h, w, x, y)
					p.extend(pns)
		return p
		
	def part2_parse(self, i):
		h, w = len(i), len(i[0])
		p = []
		for x in range(w):
			for y in range(h):
				c = i[y][x]
				if c == '*':
					# we found a gear
					pns = self.find_numbers(i, h, w, x, y)
					if len(pns) == 2:
						p.append(pns[0].n * pns[1].n)
		return p

	def part1_answer(self, i):
		k = [pn.n for pn in i]
		return sum(k)
	
	def part2_answer(self, i):
		return sum(i)
		
	def grab_number_at(self, grid, x, y):
		cx, w = x, len(grid[y])
		while cx > 0:
			if grid[y][cx - 1].isdigit():
				cx = cx - 1
			else:
				break
		sx = cx
		while cx < w - 1:
			if grid[y][cx + 1].isdigit():
				cx = cx + 1
			else:
				break
		n = int(grid[y][sx: cx + 1])
		return PartNumber(sx, y, n)
	
	def find_numbers(self, grid, h, w, x, y):
		numbers = []
		for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
			if x + dx >= 0 and x + dx < w and y + dy >= 0 and y + dy < h:
				c = grid[y + dy][x + dx]
				if c.isdigit():
					pn = self.grab_number_at(grid, x + dx, y + dy)
					if pn not in numbers:
						numbers.append(pn)
		return numbers

Today().run()
