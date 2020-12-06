#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:23:39 2020

@author: ethanhowell
"""

import sys
from utils import day4

thisModule = sys.modules[__name__]
requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
with open('/Users/ethanhowell/Documents/AOCInputs/DAY4.txt', 'r') as f:
    data = f.read()
    
lineData = data.split('\n\n')
newLineData = []
for ii in lineData:
    thisLine = ii.split('\n')
    fixedLine = ' '.join(thisLine)
    newLineData.append(fixedLine)

def part1(value):
    
    return int( value[0] in requiredFields )

def part2(value):
    
    return getattr(day4, value[0])(value[1])

base = {
    "Part1" : 0,
    "Part2" : 0
}
valid = base.copy()
for ii in newLineData:
    validFields = base.copy()
    keyVal = ii.split(' ')
    for jj in keyVal:
        newVal = jj.split(':')
        if newVal[0] != '':
            for kk in validFields.keys():
                validFields[kk] += getattr(thisModule, kk.lower())(newVal)
            
    for jj in valid.keys():
        valid[jj] += int(validFields[jj] == len(requiredFields))
print(valid)
