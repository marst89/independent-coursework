#!/usr/bin/python

import sys

salesTotalValue = 0
salesTotalNum = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    salesTotalValue += float(thisSale)
    salesTotalNum += 1
    
print salesTotalNum, "\t", salesTotalValue

