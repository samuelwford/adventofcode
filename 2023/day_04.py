import utils
import re

class Game:
	def __init__(self, line):
		a, b = line.split(':', 1)
		c, d = b.split('|', 1)
		_, gn = a.split()
		wn = c.split()
		mn = d.split()
		self.game_number = int(gn)
		self.winning_numbers = [int(i) for i in wn]
		self.my_numbers = [int(i) for i in mn]
	
	def win_count(self):
		c = [n for n in self.my_numbers if n in self.winning_numbers]
		return len(c)
	
	def points(self):
		c = [n for n in self.my_numbers if n in self.winning_numbers]
		p = int(2**(len(c) - 1))
		return p
		
class Today(utils.Day):
	def parse(self, input):
		return [Game(line) for line in input]

	def part1_answer(self, input):
		scores = [g.points() for g in input]
		return sum(scores)
	
	def part2_answer(self, input):
		cards = [1 for i in range(len(input))]
		for game in input:
			wins = game.win_count()
			multiple = cards[game.game_number - 1]
			for i in range(wins):
				j = game.game_number + i
				if j < len(cards):
					cards[j] = cards[j] + multiple
		return sum(cards)

Today().run()
