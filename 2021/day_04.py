#!/usr/bin/env python3

import utils

lines = [line for line in utils.read_input('day_04.txt')]

numbers = [int(n) for n in lines[0].split(',')]
boards = []
plays  = []

for i in range(int((len(lines) - 1) / 6)):
    rows = lines[i * 6 + 2:i * 6 + 2 + 5]
    board = [[int(row[col * 3:col * 3 + 3]) for col in range(5)] for row in rows]
    boards.append(board)
    plays.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

def check_for_win(play):
    win = False
    for i in range(5):
        if sum(play[i]) == 5:
            win = True
        if play[0][i] + play[1][i] + play[2][i] + play[3][i] + play[4][i] == 5:
            win = True
    return win

def winning_score(number, board, play):
    s = 0
    for x in range(5):
        for y in range(5):
            if play[x][y] == 0:
                s += board[x][y]
    return s * number

def play_to_win():
    for n in numbers:
        for b in range(len(boards)):
            for x in range(5):
                for y in range(5):
                    if boards[b][x][y] == n:
                        plays[b][x][y] = 1
            if check_for_win(plays[b]):
                score = winning_score(n, boards[b], plays[b])
                return score

def play_to_lose():
    last_score = 0
    winning_boards = [0 for i in range(len(boards))]
    for n in numbers:
        for b in range(len(boards)):
            for x in range(5):
                for y in range(5):
                    if boards[b][x][y] == n:
                        plays[b][x][y] = 1
            if winning_boards[b] == 0 and check_for_win(plays[b]):
                last_score = winning_score(n, boards[b], plays[b])
                winning_boards[b] = 1
        if sum(winning_boards) == len(boards):
            return last_score

print('part 1 - score:', play_to_win())
print('part 2 - score:', play_to_lose())