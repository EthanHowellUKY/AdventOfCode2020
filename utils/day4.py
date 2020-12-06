#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:27:54 2020

@author: ethanhowell
"""

import re

colors = ['amb', 'blu', 'brn', 'gry', 'gry', 'grn', 'hzl', 'oth']

def checkLen(val, lenReq):
    
    return len(val) >= lenReq

def isBetween(value, lowerBound, upperBound):
    
    return lowerBound <= int(value) <= upperBound
    
def byr(value):
    
    return int( checkLen(value, 4) and isBetween(value, 1920, 2002) )

def ecl(value):
    
    return int( value in colors )

def eyr(value):
    
    return int( checkLen(value, 4) and isBetween(value, 2020, 2030) )

def hcl(value):
    
    return int( len(value) == 7 and value[0] == '#' and bool(re.search('[0-9a-f]{6}', value[1:])) )

def hgt(value):

    if len(value) <= 2:
        return 0
    
    hgt = int(value[:-2])
    units = value[-2:]
    if units == 'cm' and isBetween(hgt, 150, 193):
        return 1
    elif units == 'in' and isBetween(hgt, 59, 76):
        return 1
    else:
        return 0

def iyr(value):
    
    return int( checkLen(value, 4) and isBetween(value, 2010, 2020) )

def pid(value):
    
    return len(value) == 9

def cid(value):
    
    return 0
    