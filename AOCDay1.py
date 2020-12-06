#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:19:41 2020

@author: ethanhowell
"""

import numpy as np

with open('/Users/ethanhowell/Documents/AOCInputs/DAY1.txt', 'r') as f:
    data = f.read()
    
lineData = data.split('\n')[:-1]
intData =[int(ii) for ii in lineData]
sortedArray = np.array(sorted(intData))

[x, y] = np.meshgrid(sortedArray, sortedArray)
z = x + y
print(np.product(y[np.where(z==2020)]))

[x, y, z] = np.meshgrid(sortedArray, sortedArray, sortedArray)
w = x + y + z
print(np.product(np.unique(y[np.where(w == 2020)])))
