#!/usr/bin/env python3


import re
import sys
import binascii

bits = 0

with open(sys.argv[1], 'r') as fin:
    data = [line.strip() for line in fin]

    for d in data:
        if len(d) > bits:
            bits = len(d)

n = 0

count0 = [0 for i in range(bits)]

for d in data:
    for i, p in enumerate(d):
        if p == '0':
            count0[i] += 1

half = len(data) / 2

gamma = []

for p in count0:
    if p > half:
        gamma.append('0')
    else:
        gamma.append('1')


epsilon = []
for p in gamma:
    if p == '0':
        epsilon.append('1')
    else:
        epsilon.append('0')

gamma = int(''.join(gamma),2)
epsilon = int(''.join(epsilon),2)


print(f'Gamma: {gamma:#b}: {gamma}')
print(f'Epsilon: {epsilon:#b}: {epsilon}')
print(f'Count 0: {count0}')

print(epsilon * gamma)