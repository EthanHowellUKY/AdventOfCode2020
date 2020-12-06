#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:07:48 2020

@author: ethanhowell
"""

import numpy as np

with open('/Users/ethanhowell/Documents/AOCInputs/DAY5.txt', 'r') as f:
    data = f.read()
    
finalRows = []
finalCols = []
boardingPasses = []
lineData = data.split('\n')[0:-1]
mapping = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}

for ii in lineData:
    rows = ii[0:7]
    cols = ii[7:]
    for key, val in mapping.items():
        rows = rows.replace(key, val)
        cols = cols.replace(key, val)
    boardingPasses.append(int(rows, 2)*8 + int(cols, 2))
print(max(boardingPasses))

sortedPasses = np.array(sorted(boardingPasses))
mySeatList = np.arange(min(boardingPasses), min(boardingPasses)+len(boardingPasses))

mySeat = mySeatList[np.where((sortedPasses - mySeatList)==1)][0]
print(mySeat)
