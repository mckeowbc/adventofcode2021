#!/usr/bin/env python3

import sys

def printFish(fish : list, prompt : str) -> None:
    print("{prompt}: {fish}".format(prompt=prompt,fish=','.join(map(str,fish))))

with open(sys.argv[1],'r') as fin:
    fish = fin.readline().strip()
    fish = list(map(int,fish.split(',')))


days = int(sys.argv[2])


printFish(fish,'Initial State')


for dn in range(days):
    for i in range(len(fish)):
        fish[i] -= 1
    
    for i in range(len(fish)):
        if fish[i] == -1:
            fish[i] = 6
            fish.append(8)

    printFish(fish, 'After %4d days' % (dn+1))


print(len(fish))