#!/usr/bin/env python3


import sys
import re

data = []

with open(sys.argv[1],'r') as fin:
    for line in fin:
        line = line.strip()
        (patterns, values) = re.split(r'\s*\|\s*',line)

        patterns = [''.join(sorted(p)) for p in re.split(r'\s+',patterns)]
        values   = [''.join(sorted(v)) for v in re.split(r'\s+',values)]

        data.append((patterns,values))


import pprint
#pprint.pprint(data)

count = 0
for obs in data:
    for d in obs[1]:
        if len(d) in (2,3,4,7):
            count += 1

print(count)