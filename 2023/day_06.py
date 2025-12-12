import utils

class Today(utils.Day):
    def parse(self, data):
        times = [int(i) for i in data[0][9:].split()]
        distances = [int(i) for i in data[1][9:].split()]
        result = list(zip(times, distances))
        return result
    
    def part1_answer(self, i):
        wins = []
        for t, d in i:
            w = 0
            for i in range(1, t):
                j = (t - i) * i
                if j > d:
                    w = w + 1
            wins.append(w)
        a = 1
        for w in wins:
            a = a * w
        return a

    def part2_parse(self, data):
        time = int(''.join(data[0][9:].split()))
        distance = int(''.join(data[1][9:].split()))
        return [(time, distance)]
    
    def part2_answer(self, i):
        t, d = i[0]
        w = 0
        for i in range(1, t):
            j = (t - i) * i
            if j > d:
                w = w + 1
        return w

Today().run()