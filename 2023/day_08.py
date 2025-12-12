import utils
import functools

class Today(utils.Day):
    def parse(self, data):
        tree = {}
        steps = data[0]
        c = 2
        while c < len(data):
            n, l, r = data[c][0:3], data[c][7:10], data[c][12:15]
            tree[n] = (l, r)
            c = c + 1
        return (steps, tree)
    
    def part1_answer(self, data):
        steps, tree = data
        c, i = 0, 0
        n = 'AAA'
        while n != 'ZZZ':
            l, r = tree[n]
            s = steps[i]
            c = c + 1
            i = i + 1 if i < (len(steps) - 1) else 0
            if s == 'L':
                n = l
            else:
                n = r
        return c
    
    def number_of_steps(n, steps, tree):
        c, i = 0, 0
        while n[-1] != 'Z':
            l, r = tree[n]
            s = steps[i]
            c = c + 1
            i = i + 1 if i < (len(steps) - 1) else 0
            if s == 'L':
                n = l
            else:
                n = r
        return c

    def gcd(a,b):
        if b == 0:
            return a
        return Today.gcd(b, a % b)

    def lcm(x, y):
        return x * y / Today.gcd(x, y)

    def part2_answer(self, data):
        steps, tree = data
        c, i = 0, 0
        n = [x for x in tree.keys() if x[-1] == 'A']
        s = [Today.number_of_steps(x, steps, tree) for x in n]
        a = functools.reduce(Today.lcm, s)
        return int(a)
    
Today().run()