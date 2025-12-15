file = "/Users/sford/Developer/adventofcode/2025/inputs/day_06.txt"

def product(lst):
    p = 1
    for n in lst:
        p *= n
    return p

stream = open(file, 'rt')
rows = [list(map(int, line.strip().split())) if any(ch.isnumeric() for ch in line) else line.strip().split() 
        for line in stream.readlines()]
stream.close()

problems = [[0 for j in range(len(rows))] for i in range(len(rows[0]))]
for i, row in enumerate(rows):
    for j, col in enumerate(row):
        problems[j][i] = rows[i][j]

checksum = 0
for problem in problems:
    if problem[-1] == '*':
        checksum += product(problem[:-1])
    else:
        checksum += sum(problem[:-1])
print(f"Part 1: {checksum}")

stream = open(file,'rt')
rows = [line for line in stream.readlines()]
stream.close()
rows = [line[:-1] if line[-1] == '\n' else line + ' ' for line in rows]

human_math_list = []
num_list = []
for j in range(len(rows[0]) - 1, -1, -1):
    if all(rows[r][j].isspace() for r in range(len(rows))):
        human_math_list.append(num_list)
        num_list = []
        continue
    num = ''
    for i in range(len(rows)):
        try:
            if rows[i][j].isnumeric():
                num += rows[i][j]
            if rows[i][j] in '+*':
                num_list.insert(0, rows[i][j])
        except:
            print(f"culprit: {j=}")
    num_list.append(num)
    if j == 0:
        human_math_list.append(num_list)

checksum = 0
for problem in human_math_list:
    if problem[0] == '+':
        checksum += sum(list(map(int, problem[1:])))
    else:
        checksum += product(list(map(int, problem[1:])))
print(f"Part 2: {checksum}")