#!/usr/bin/env python3

import sys
import re

def printGrid(grid : list) -> None:
    for row in grid:
        print('  '.join(map(lambda x : '%5d' % x, row)))

def countDanger(grid : list) -> int:
    danger = 0
    for row in grid:
        for col in row:
            if col > 1:
                danger += 1
    return danger

lines = []
grid  = []

maxx = 0
maxy = 0

with open(sys.argv[1], 'r') as fin:
    for line in fin:
        m = re.match(r'^(?P<startx>\d+),(?P<starty>\d+)\s*->\s*(?P<endx>\d+),(?P<endy>\d+)', line)

        if m:
            points = m.groupdict()
            for key,value in points.items():
                points[key] = int(value)

            lines.append(points)

            if int(points['startx']) > maxx:
                maxx = points['startx']
            if int(points['endx']) > maxx:
                maxx = points['endx']
            if int(points['starty']) > maxy:
                maxy = points['starty']
            if int(points['endy']) > maxy:
                maxy = points['endy']

print(f'Max X: {maxx}')
print(f'Max Y: {maxy}')



for i in range(maxy+1):
    grid.append([0 for i in range(maxx+1)])

for i, line in enumerate(lines):
    print(f'Adding line: {i} to grid ({line["startx"]},{line["starty"]} -> {line["endx"]},{line["endy"]})')
    if line['startx'] == line['endx']:  # vertical
        x = line['startx']
        
        if line['starty'] > line['endy']:
            line['starty'], line['endy'] = line['endy'], line['starty']
        for y in range(line['starty'], line['endy']+1):
           grid[y][x] += 1
    elif line['starty']== line['endy']: # horizontal
        y = line['starty']
        if line['startx'] > line['endx']:
            line['startx'], line['endx'] = line['endx'], line['startx']
        for x in range(line['startx'], line['endx']+1):
            grid[y][x] += 1
    else:
        xdir = 1 if line['startx'] <= line['endx'] else -1
        ydir = 1 if line['starty'] <= line['endy'] else -1
        for x,y in zip(range(line['startx'], line['endx'] + xdir, xdir), range(line['starty'], line['endy'] + ydir, ydir)):
            grid[y][x] += 1
        
#printGrid(grid) 
print(countDanger(grid))