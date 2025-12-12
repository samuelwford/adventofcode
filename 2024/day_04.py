import os
import utils

class Today(utils.Day):
	def __init__(self):
		day = os.path.splitext(os.path.basename(__file__))[0]
		super().__init__(day)
		
	def parse(self, data):
		return data
		
	def lookForWordInPuzzleAt(self, word, puzzle, location):
		sx, sy = location
		h = len(puzzle)
		w = len(puzzle[0])
		matches = 0
		
		for dx, dy in [(1,0), (1,1), (0,1), (-1,1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
			l = 0
			for i in range(len(word)):
				x = sx + i * dx
				y = sy + i * dy
				if x < 0 or x == w or y < 0 or y == h:
					break
				if puzzle[y][x] == word[i]:
					l += 1
				else:
					break
					
			if l == len(word):
				matches += 1
		
		return matches
	
	def isXMasAt(self, puzzle, location):
		x, y = location
		h = len(puzzle)
		w = len(puzzle[0])

		if puzzle[y][x] != 'A':
			return False
					
		d1 = (puzzle[y-1][x-1] == 'M' and puzzle[y+1][x+1] == 'S') or (puzzle[y-1][x-1] == 'S' and puzzle[y+1][x+1] == 'M')
		d2 = (puzzle[y+1][x-1] == 'M' and puzzle[y-1][x+1] == 'S') or (puzzle[y+1][x-1] == 'S' and puzzle[y-1][x+1] == 'M')
					
		return d1 and d2
		
	def part1_answer(self, data):
		h = len(data)
		w = len(data[0])
		found = 0
		
		for x in range(w):
			for y in range(h):
				found += self.lookForWordInPuzzleAt('XMAS', data, (x, y))
		
		return found
		
	def part2_answer(self, data):
		h = len(data)
		w = len(data[0])
		found = 0
	
		for x in range(1, w-1):
			for y in range(1, h-1):
				found += self.isXMasAt(data, (x,y))
		
		return found
