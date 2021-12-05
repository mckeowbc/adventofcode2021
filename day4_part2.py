#!/usr/bin/env python3

import re
import sys
import pprint

boards = []
called = []
winners = []

def getWinningGroup(board : list) -> bool:
    for row in board:
        if all(map(lambda x : x['marked'], row)):
            return row
    
    for col in range(5):
        if all(map(lambda x: x[col]['marked'], board)):
            return [row[col] for row in board]
    return None

def checkBoard(board : list) -> bool:
    group = getWinningGroup(board)

    return group is not None



with open(sys.argv[1], 'r') as fin:
    called = map(int,fin.readline().strip().split(','))

    board = []
    for line in fin:
        line = line.strip()
        if re.match(r'^\s*$', line):
            if board:
                boards.append(board)
                board = []
        elif re.match(r'^\d+\s+\d+\s+\d+\s*\d+',line):
            nums = re.split(r'\s+', line)
            board.append([])
            for n in nums:
                board[-1].append({ 'num': int(n), 'marked' : False})
    if board:
        boards.append(board)

bingo = False

for n in called:
    print(f'Called: {n}')
    for board in boards:
        for row in board:
            for col in row:
                if col['num'] == n:
                    col['marked'] = True

    for i,board in enumerate(boards):
        if i not in winners and checkBoard(board):
            print(f'Bingo !: Board {i}')
            winners.append(i)
            sum = 0

            for row in board:
                for col in row:
                    if col['marked'] == False:
                        sum += col['num']
                        
            print(f'Final Score: {sum * n}')

            
    if len(winners) == len(boards):
        break

