#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 01:03:41 2020

@author: ethanhowell
"""

import collections

with open("/Users/ethanhowell/Documents/AOCInputs/DAY6.txt", "r") as f:
    data = f.read()
    
groupData = data.split('\n\n')
newData = []
for ii in groupData:
    tempLine = ''.join(ii.split('\n'))
    newData.append(tempLine)
    
summation = 0
for ii in newData:
    thisDict = collections.Counter(ii)
    summation+=len(thisDict.keys())
print(summation)
    
summation = 0
for ii in groupData:
    tempLine = ii.split('\n')
    if len(tempLine) == 1:
        thisDict = collections.Counter(tempLine[0])
        summation+=len(thisDict.keys())
    else:
        thisDict = collections.Counter(''.join(tempLine))
        if '' in tempLine:
            tempLine.remove('')
        summation+=len([xx for xx, yy in thisDict.items() if yy == len(tempLine)])
print(summation)