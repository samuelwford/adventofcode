import os
import utils

class Today(utils.Day):
	def __init__(self):
		day = os.path.splitext(os.path.basename(__file__))[0]
		super().__init__(day)
		
	def parse(self, data):
		return [list(x) for x in data]
	
	def findguard(self, grid):
		for y, row in enumerate(grid):
			if '^' in row:
				x = row.index('^')
				return (x, y)
	
	def printgrid(self, grid):
		x = [''.join(i) for i in grid]
		y = '\n'.join(x)
		print('----------')
		print(y)

	def patrol(self, grid):
		gx, gy = self.findguard(grid)
		ds = [(0, -1), (1, 0), (0, 1), (-1, 0)]
		d = 0
		w, h = len(grid[0]), len(grid)
		
		while True:
			grid[gy][gx] = 'X'
			dx, dy = ds[d]
			lx, ly = gx + dx, gy + dy
			
			# if that's off the map, we're done
			if lx < 0 or lx == w or ly < 0 or ly == h:
				return grid
			
			# rotate if we hit an obstacle
			if grid[ly][lx] == '#':
				d += 1
				if d == 4:
					d = 0
			else:
				gx, gy = lx, ly
		
	def patrolforloops(self, grid):
		sx, sy = self.findguard(grid)
		gx, gy = sx, sy
		ds = [(0, -1, '|'), (1, 0, '-'), (0, 1, '|'), (-1, 0, '-')] # W S E N
		d = 0
		w, h = len(grid[0]), len(grid)
		
		# keep a stack of every turn: where it happened & which direction
		# on each step, look backwards in the stack to see if a turn might head 
		# back to a previous turn that's 1 turn ahead
		# make sure the path to that spot is clear
		turnstack = []
		loops = 0
		
		while True:
			dx, dy, dm = ds[d]
			
			if grid[gy][gx] == '.':
				grid[gy][gx] = dm
			else:
				grid[gy][gx] = '+'
				
			lx, ly = gx + dx, gy + dy
			
			# if that's off the map, we're done
			if lx < 0 or lx == w or ly < 0 or ly == h:
				grid[sy][sx] = '^'
				return loops
			
			# rotate if we hit an obstacle
			if grid[ly][lx] == '#':
				turnstack.append((gx, gy, d))				
				d = (d + 1) % 4
				grid[gy][gx] = '+'
				
			else:
				# we're not turning, look back through all the turns to see
				# we can turn into a previous turn
				
				if len(turnstack) > 2:
					for lb in range(len(turnstack) - 2):
						wx, wy, wd = turnstack[lb]
						
						# going W, look for a previous turn E with a clear path N
						if d == 0 and wd == 2 and gx == wx and self.is_clear_shot(grid, (gx, gy), (wx, wy), ds[3]):
							self.preview(grid, (gx, gy), ds[3])
							loops += 1
							
						# going S, look for a previous turn W with a clear path W
						if d == 1 and wd == 3 and gy == wy and self.is_clear_shot(grid, (gx, gy), (wx, wy), ds[0]):
							self.preview(grid, (gx, gy), ds[0])
							loops += 1

						# going E, look for a previous turn W with a clear path S
						if d == 2 and wd == 0 and gx == wx and self.is_clear_shot(grid, (gx, gy), (wx, wy), ds[1]):
							self.preview(grid, (gx, gy), ds[1])
							loops += 1
														
						# going N, look for a previous turn S with a clear path E
						if d == 3 and wd == 1 and gy == wy and self.is_clear_shot(grid, (gx, gy), (wx, wy), ds[2]):
							self.preview(grid, (gx, gy), ds[2])
							loops += 1
						
				gx, gy = lx, ly

	def preview(self, grid, p, d):
		x, y = p
		dx, dy, _ = d
		gx, gy = x + dx, y + dy
		
		t1 = grid[gy][gx]
		t2 = grid[y][x]
		grid[gy][gx] = 'O'
		grid[y][x] = '^'
		self.printgrid(grid)
		grid[gy][gx] = t1
		grid[y][x] = t2
		
	def is_clear_shot(self, grid, p1, p2, d):
		x1, y1 = p1
		x2, y2 = p2
		dx, dy, _ = d
		
		while x1 != x2 or y2 != y2:
			x1 += dx
			y1 += dy
			if grid[y1][x1] == '#':
				return False
		
		return True
		
	def part1_answer(self, data):
		grid = self.patrol(data)
		answer = sum(row.count('X') for row in grid)
		return answer
		
	def part2_answer(self, data):
		loops = self.patrolforloops(data)		
		return loops