#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:35:45 2020

@author: ethanhowell
"""

import collections

with open('/Users/ethanhowell/Documents/AOCInputs/DAY2.txt', 'r') as f:
    data = f.read()
    
valid = {
    'Part1' : 0,
    'Part2': 0
}
lineData = data.split('\n')[:-1]
for line in lineData:
    [rangeVals, char, password] = line.split(' ')
    rangeVals = rangeVals.split('-')
    minVal = int(rangeVals[0])
    maxVal = int(rangeVals[1])
    
    collect = collections.Counter(password)
    if minVal <= collect[char[0]] <= maxVal:
        valid['Part1'] += 1
    if password[minVal-1] == char[0] and password[maxVal-1] == char[0]:
        pass
    elif password[minVal-1] == char[0] or password[maxVal-1] == char[0]:
        valid['Part2'] += 1
        
print(valid)
    