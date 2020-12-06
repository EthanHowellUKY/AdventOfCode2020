#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:44:22 2020

@author: ethanhowell
"""

with open('/Users/ethanhowell/Documents/AOCInputs/DAY3.txt', 'r') as f:
    data = f.read()
    
ranges = [(1,1), (1,3), (1,5), (1,7), (2,1)]
lineData = data.split('\n')[:-1]

treeMultiplier = 1
lineLen = max([len(ii) for ii in lineData])
for startRow, startCol in ranges:
    trees = 0
    thisCol = startCol
    colIter = startCol
    for ii in range(startRow, len(lineData), startRow):
        if thisCol >= lineLen:
            thisCol = thisCol - lineLen
        if lineData[ii][thisCol] == '#':
            trees+=1
        thisCol += colIter
    treeMultiplier *= trees
    print(trees)
print(treeMultiplier)
