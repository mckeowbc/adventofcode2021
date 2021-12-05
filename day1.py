#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], 'r') as fin:
    data = [line.strip() for line in fin]


data = list(
        map(lambda i : int(i), 
            filter(lambda x : re.match('^\d+$', x),data)
        )
    )

count = 0
cur   = data[0]

for n in data[1:]:
    if n > cur:
        count += 1
    cur = n

print(count)