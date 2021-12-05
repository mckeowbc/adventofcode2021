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


gammaArray = getGammaArray(data)
epsilonArray = getEpsilonArray(gammaArray)


gamma = int(''.join(gammaArray),2)
epsilon = int(''.join(epsilonArray),2)


print(f'Gamma: {gamma:#b}: {gamma}')
print(f'Epsilon: {epsilon:#b}: {epsilon}')

print(epsilon * gamma)



import copy

o2_rates = copy.copy(data)
bn = 0
while len(o2_rates) > 1:
    gamma = getGammaArray(o2_rates)

    o2_rates = list(filter(lambda x : x[bn] == gamma[bn], o2_rates))
    bn += 1

print(o2_rates)

co2_rates = copy.copy(data)
bn = 0
while len(co2_rates) > 1:
    gamma = getEpsilonArray(getGammaArray(co2_rates))

    co2_rates = list(filter(lambda x : x[bn] == gamma[bn], co2_rates))
    bn += 1

print(co2_rates)

print(int(o2_rates[0],2) * int(co2_rates[0], 2))
