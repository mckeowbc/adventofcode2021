#!/usr/bin/env python3


import re
import sys
import binascii


def getGammaArray(data:list) -> list:
    bits = 0
    
    for d in data:
        if len(d) > bits:
            bits = len(d)

    count0 = [0 for i in range(bits)]
    half = len(data) / 2

    for d in data:
        for i, p in enumerate(d):
            if int(p) == 0:
                count0[i] += 1
    gamma = []
    for p in count0:
        if p > half:
            gamma.append('0')
        else:
            gamma.append('1')
    return gamma

def getEpsilonArray(gammaArray:list) -> list:
    epsilon = []
    for p in gammaArray:
        if p == '0':
            epsilon.append('1')
        else:
            epsilon.append('0')
    return epsilon


with open(sys.argv[1], 'r') as fin:
    data = [line.strip() for line in fin]


gamma = getGammaArray(data)
epsilon = getEpsilonArray(gamma)


gamma = int(''.join(gamma),2)
epsilon = int(''.join(epsilon),2)


print(f'Gamma: {gamma:#b}: {gamma}')
print(f'Epsilon: {epsilon:#b}: {epsilon}')

print(epsilon * gamma)