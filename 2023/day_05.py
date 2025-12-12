import utils

class SeedMap:
    def __init__(self):
        self.from_type = ''
        self.to_type = ''
        self.all_ranges = []

class Today(utils.Day):
    def parse(self, input):
        line = input[0][6:]
        seeds = [int(s) for s in line.split()]
        line_no = 2
        all_maps = {}
        current_map = SeedMap()
        while line_no < len(input):
            line = input[line_no]
            line_no = line_no + 1
            if line == '':
                all_maps[current_map.from_type] = current_map
                current_map = SeedMap()
            elif line[0].isalpha():
                i, _ = line.split()
                f, _, t = i.split('-')
                current_map.from_type = f
                current_map.to_type = t
            elif line[0].isdigit():
                r = [int(i) for i in line.split()]
                current_map.all_ranges.append(r)
        if current_map.from_type != '':
            all_maps[current_map.from_type] = current_map
        return [seeds, all_maps]

    def part1_answer(self, input):
        seeds, all_maps = input
        locations = [self.compute_location(seed, all_maps) for seed in seeds]
        return min(locations)

    def part2_answer(self, input):
        seeds, all_maps = input
        seed_pairs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds) - 1, 2)]
        locations = [self.compute_location_with_range(i, j, all_maps) for i, j in seed_pairs]
        starts = [i for i, j in locations[0]]
        return min(starts)
    
    def compute_location(self, seed, maps):
        f = 'seed'
        v = seed
        while f != 'location':
            m = maps[f]
            for d, s, r in m.all_ranges:
                if v >= s and v <= s + r:
                    v = v - s + d
                    break
            f = m.to_type
        return v
    
    def compute_location_with_range(self, seed_start, seed_run, maps):
        f = 'seed'
        v = [(seed_start, seed_start + seed_run)]
        while f != 'location':
            m = maps[f]
            n = []
            for a, b in v:
                for e, c, r in m.all_ranges:
                    d = c + r
                    # map overlapping source ranges to destination ranges
                    # does this range over lap? then split into as many ranges as necessary
                    if a > d or b < c:
                        # no overlap, pass through as is
                        n.append((a, b))
                    else:
                        # some overlap, split as needed
                        if a < c:
                            n.append((a, c - 1))
                            a = c
                        if b > d:
                            n.append((d + 1, b))
                            b = d
                        n.append((a - c + r, b - c + r))
            v = list(set(n))
            f = m.to_type
        return v

Today().run()
