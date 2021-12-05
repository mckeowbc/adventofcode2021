#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1], 'r') as fin:
    commands = [line.strip() for line in fin]


horizontal, depth = 0,0

for command in commands:
    m = re.match(r'^(?P<command>\w+)\s*(?P<num>\d+)',command)

    if m:
        direction = m.groupdict()['command']
        number    = int(m.groupdict()['num'])

        if direction == 'forward':
            horizontal += number
        elif direction == 'down':
            depth += number
        elif direction == 'up':
            depth -= number


print(f'Horizontal Postion: {horizontal}')
print(f'Depth: {depth}')

print(f'Answer: {horizontal * depth}')
    