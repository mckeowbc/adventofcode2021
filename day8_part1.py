#!/usr/bin/env python3


import sys
import re
import pprint

data = []

def determineWireConnections(obs : list) -> dict:
    mapping = {
    }

    while len(mapping) < 10:
        for ob in obs:
            if ob in mapping.values():
                continue

            if len(ob) == 2:
                mapping[1] = ob
            elif len(ob) == 3:
                mapping[7] = ob
            elif len(ob) == 4:
                mapping[4] = ob
            elif len(ob) == 7:
                mapping[8] = ob
            elif len(ob) == 5 and 7 in mapping and mapping[7] <= ob:
                mapping[3] = ob
            elif len(ob) == 5 and 9 in mapping and ob <= mapping[9]:
                mapping[5] = ob
            elif len(ob) == 5 and 5 in mapping and 3 in mapping:
                mapping[2] = ob
            elif len(ob) == 6 and 7 in mapping and not mapping[7] <= ob:
                mapping[6] = ob
            elif len(ob) == 6 and 3 in mapping and mapping[3] <= ob:
                 mapping[9] = ob
            elif len(ob) == 6 and 9 in mapping and 6 in mapping:
                mapping[0] = ob
    return mapping

def getDigit(connections: dict, value : set) -> int:
    for (k,v) in connections.items():
        if value == v:
            return k
            

with open(sys.argv[1],'r') as fin:
    for line in fin:
        line = line.strip()
        (patterns, values) = re.split(r'\s*\|\s*',line)

        patterns = [set(p) for p in re.split(r'\s+',patterns)]
        values   = [set(v) for v in re.split(r'\s+',values)]

        data.append((patterns,values))


import pprint
#pprint.pprint(data)

count = 0
for obs in data:
    for d in obs[1]:
        if len(d) in (2,3,4,7):
            count += 1

print(count)

total = 0

for obs in data:
    connections = determineWireConnections(obs[0])
    digits = [getDigit(connections, v) for v in obs[1]]
    num = int(''.join(map(str,digits)))
    total += num
    print(num)

print(f"Total: {total}")