#!/usr/bin/env python

import sys
import re

with open(sys.argv[1], 'r') as fin:
    data = [line.strip() for line in fin]


data = list(
        map(lambda i : int(i), 
            filter(lambda x : re.match('^\d+$', x),data)
        )
    )

sums = []
for i in range(2,len(data)):
    sum3 = data[i] + data[i-1] + data[i-2]
    sums.append(sum3)


count = 0
cur   = sums[0]

for n in sums[1:]:
    if n > cur:
        count += 1
    cur = n

print(count)