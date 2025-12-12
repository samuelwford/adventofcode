import utils

class Hand:
    ranks = '23456789TJQKA'

    def __init__(self, i):
        j, k = i.split()
        self.cards = j
        self.bid = int(k)

    def strength(self):
        m = {}
        for c in self.cards:
            if c in m:
                m[c] = m[c] + 1
            else:
                m[c] = 1
        c2, c3, c4, c5 = 0, 0, 0, 0
        for k, v in m.items():
            if v == 2: c2 = c2 + 1
            if v == 3: c3 = 1
            if v == 4: c4 = 1
            if v == 5: c5 = 1
        s = 0
        if c5 == 1: s = 6
        elif c4 == 1: s = 5
        elif c3 == 1 and c2 == 1: s = 4
        elif c3 == 1: s = 3
        elif c2 == 2: s = 2
        elif c2 == 1: s = 1
        return s
    
    def compare(self, other):
        s1, s2 = self.strength(), other.strength()
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            # same strength, now compare cards
            c = 0
            while c < 5:
                c1, c2 = self.cards[c], other.cards[c]
                r1, r2 = Hand.ranks.find(c1), Hand.ranks.find(c2)
                c = c + 1
                if r1 == r2: continue
                if r1 < r2: return -1
                if r1 > r2: return 1
             
    def __eq__(self, other):
        return self.compare(other) == 0
    
    def __lt__(self, other):
        return self.compare(other) == -1
    
class JokerHand:
    ranks = 'J23456789TQKA'

    def __init__(self, i):
        j, k = i.split()
        self.cards = j
        self.bid = int(k)

    def strength(self):
        if self.cards == '23J68':
            print('pause here')
        m = {}
        for c in self.cards:
            if c in m:
                m[c] = m[c] + 1
            else:
                m[c] = 1
        c2, c3, c4, c5 = 0, 0, 0, 0
        jc = m['J'] if 'J' in m else 0
        for k, v in m.items():
            jp = jc if k != 'J' else 0
            if v + jp == 5: 
                c5 = 1
                jc = jc = (5 - v)
                continue
            if v + jp == 4: 
                c4 = 1
                jc = jc - (4 - v)
                continue
            if v + jp == 3:
                c3 = 1
                jc = jc - (3 - v)
                continue
            if v + jp == 2: 
                c2 = c2 + 1
                jc = jc - 1
        s = 0
        if c5 == 1: s = 6
        elif c4 == 1: s = 5
        elif c3 == 1 and c2 == 1: s = 4
        elif c3 == 1: s = 3
        elif c2 == 2: s = 2
        elif c2 == 1: s = 1
        return s
    
    def compare(self, other):
        s1, s2 = self.strength(), other.strength()
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            # same strength, now compare cards
            c = 0
            while c < 5:
                c1, c2 = self.cards[c], other.cards[c]
                r1, r2 = JokerHand.ranks.find(c1), JokerHand.ranks.find(c2)
                c = c + 1
                if r1 == r2: continue
                if r1 < r2: return -1
                if r1 > r2: return 1
             
    def __eq__(self, other):
        return self.compare(other) == 0
    
    def __lt__(self, other):
        return self.compare(other) == -1

class Today(utils.Day):
    def parse(self, data):
        return [Hand(i) for i in data]

    def part1_answer(self, data):
        data.sort()
        w = 0
        for i, h in enumerate(data):
            w = w + (h.bid * (i + 1))
        return w
    
    def part2_parse(self, data):
        return [JokerHand(i) for i in data]

    def part2_answer(self, data):
        data.sort()
        w = 0
        for i, h in enumerate(data):
            print('hand', i, ':', h.cards, ', strength', h.strength(), ', bid', h.bid, '*', i + 1, ', winnings', h.bid * (i + 1))
            w = w + (h.bid * (i + 1))
        # input('pause')
        return w
        
    
Today().run()