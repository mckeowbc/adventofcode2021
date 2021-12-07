#!/usr/bin/env python3

import sys

def printFish(fish : list, prompt : str) -> None:
    print("{prompt}: {fish}".format(prompt=prompt,fish=','.join(map(str,fish))))

with open(sys.argv[1],'r') as fin:
    fish = fin.readline().strip()
    fish = list(map(int,fish.split(',')))


fishctx = [0 for i in range(9)]

for f in fish:
    fishctx[f] += 1

days = int(sys.argv[2])


for dn in range(days):
    print(fishctx)
    fish0 = fishctx[0]
    fishctx = fishctx[1:]
    fishctx.append(fish0)
    fishctx[6] += fish0

print(sum(fishctx))