#============================================ test monkeys
#Monkey 0:
#  Starting items: 79, 98
#  Operation: new = old * 19
#  Test: divisible by 23
#    If true: throw to monkey 2
#    If false: throw to monkey 3
#
#Monkey 1:
#  Starting items: 54, 65, 75, 74
#  Operation: new = old + 6
#  Test: divisible by 19
#    If true: throw to monkey 2
#    If false: throw to monkey 0
#
#Monkey 2:
#  Starting items: 79, 60, 97
#  Operation: new = old * old
#  Test: divisible by 13
#    If true: throw to monkey 1
#    If false: throw to monkey 3
#
#Monkey 3:
#  Starting items: 74
#  Operation: new = old + 3
#  Test: divisible by 17
#    If true: throw to monkey 0
#    If false: throw to monkey 1

#=============================================== real monkeys
#Monkey 0:
#  Starting items: 56, 52, 58, 96, 70, 75, 72
#  Operation: new = old * 17
#  Test: divisible by 11
#    If true: throw to monkey 2
#    If false: throw to monkey 3
#
#Monkey 1:
#  Starting items: 75, 58, 86, 80, 55, 81
#  Operation: new = old + 7
#  Test: divisible by 3
#    If true: throw to monkey 6
#    If false: throw to monkey 5
#
#Monkey 2:
#  Starting items: 73, 68, 73, 90
#  Operation: new = old * old
#  Test: divisible by 5
#    If true: throw to monkey 1
#    If false: throw to monkey 7
#
#Monkey 3:
#  Starting items: 72, 89, 55, 51, 59
#  Operation: new = old + 1
#  Test: divisible by 7
#    If true: throw to monkey 2
#    If false: throw to monkey 7
#
#Monkey 4:
#  Starting items: 76, 76, 91
#  Operation: new = old * 3
#  Test: divisible by 19
#    If true: throw to monkey 0
#    If false: throw to monkey 3
#
#Monkey 5:
#  Starting items: 88
#  Operation: new = old + 4
#  Test: divisible by 2
#    If true: throw to monkey 6
#    If false: throw to monkey 4
#
#Monkey 6:
#  Starting items: 64, 63, 56, 50, 77, 55, 55, 86
#  Operation: new = old + 8
#  Test: divisible by 13
#    If true: throw to monkey 4
#    If false: throw to monkey 0
#
#Monkey 7:
#  Starting items: 79, 58
#  Operation: new = old + 6
#  Test: divisible by 17
#    If true: throw to monkey 1
#    If false: throw to monkey 5

def test_monkeys():
	return ([[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]], [0, 0, 0, 0])

def test_round(ms, c):
	for i in range(len(ms)):
		m = ms[i]
		for j in m:
			c[i] += 1
			if i == 0:
				j = (j * 19) // 3
				if j % 23 == 0:
					ms[2].append(j)
				else:
					ms[3].append(j)
			elif  i == 1:
				j = (j + 6) // 3
				if j % 19 == 0:
					ms[2].append(j)
				else:
					ms[0].append(j)
			elif  i == 2:
				j = (j * j) // 3
				if j % 13 == 0:
					ms[1].append(j)
				else:
					ms[3].append(j)
			elif  i == 3:
				j = (j + 3) // 3
				if j % 17 == 0:
					ms[0].append(j)
				else:
					ms[1].append(j)
		ms[i] = []

def real_monkeys():
	ms = [ \
		[56, 52, 58, 96, 70, 75, 72], \
		[75, 58, 86, 80, 55, 81], \
		[73, 68, 73, 90], \
		[72, 89, 55, 51, 59], \
		[76, 76, 91], \
		[88], \
		[64, 63, 56, 50, 77, 55, 55, 86], \
		[79, 58], \
		]
	cs = [0, 0, 0, 0, 0, 0, 0, 0]
	return (ms, cs)

def real_round(ms, cs):
	for i in range(len(ms)):
		m = ms[i]
		for j in m:
			cs[i] += 1
			if i == 0:
				j = (j * 17) // 3
				if j % 11 == 0:
					ms[2].append(j)
				else:
					ms[3].append(j)
			elif  i == 1:
				j = (j + 7) // 3
				if j % 3 == 0:
					ms[6].append(j)
				else:
					ms[5].append(j)
			elif  i == 2:
				j = (j * j) // 3
				if j % 5 == 0:
					ms[1].append(j)
				else:
					ms[7].append(j)
			elif  i == 3:
				j = (j + 1) // 3
				if j % 7 == 0:
					ms[2].append(j)
				else:
					ms[7].append(j)
			elif  i == 4:
				j = (j * 3) // 3
				if j % 19 == 0:
					ms[0].append(j)
				else:
					ms[3].append(j)		
			elif  i == 5:
				j = (j + 4) // 3
				if j % 2 == 0:
					ms[6].append(j)
				else:
					ms[4].append(j)		
			elif  i == 6:
				j = (j + 8) // 3
				if j % 13 == 0:
					ms[4].append(j)
				else:
					ms[0].append(j)
			elif  i == 7:
				j = (j + 6) // 3
				if j % 17 == 0:
					ms[1].append(j)
				else:
					ms[5].append(j)					
		ms[i] = []

def real_round2(ms, cs):
	lcd = 11 * 3 * 5 * 7 * 19 * 2 * 13 * 17
	for i in range(len(ms)):
		m = ms[i]
		for j in m:
			cs[i] += 1
			j %= lcd
			if i == 0:
				j = (j * 17)
				if j % 11 == 0:
					ms[2].append(j)
				else:
					ms[3].append(j)
			elif  i == 1:
				j = (j + 7)
				if j % 3 == 0:
					ms[6].append(j)
				else:
					ms[5].append(j)
			elif  i == 2:
				j = (j * j)
				if j % 5 == 0:
					ms[1].append(j)
				else:
					ms[7].append(j)
			elif  i == 3:
				j = (j + 1)
				if j % 7 == 0:
					ms[2].append(j)
				else:
					ms[7].append(j)
			elif  i == 4:
				j = (j * 3)
				if j % 19 == 0:
					ms[0].append(j)
				else:
					ms[3].append(j)		
			elif  i == 5:
				j = (j + 4)
				if j % 2 == 0:
					ms[6].append(j)
				else:
					ms[4].append(j)		
			elif  i == 6:
				j = (j + 8)
				if j % 13 == 0:
					ms[4].append(j)
				else:
					ms[0].append(j)
			elif  i == 7:
				j = (j + 6)
				if j % 17 == 0:
					ms[1].append(j)
				else:
					ms[5].append(j)					
		ms[i] = []

def p1():
	ms, cs = test_monkeys()
	for _ in range(20):
		test_round(ms, cs)
	print(cs)
	print('part 1 test:', cs[0] * cs[3])
	
	ms, cs = real_monkeys()
	for _ in range(20):
		real_round(ms, cs)
	cs.sort()
	print(cs)
	m1, m2 = cs[-2:]
	print('part 1:', m1 * m2)
	
def p2():
	ms, cs = real_monkeys()
	for _ in range(10000):
		real_round2(ms, cs)
	cs.sort()
	print(cs)
	m1, m2 = cs[-2:]
	print('part 2:', m1 * m2)
		
p1()
p2()
