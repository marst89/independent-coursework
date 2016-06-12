#!/usr/bin/python

import sys

itemsTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisItem = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", itemsTotal
        oldKey = thisKey;
        itemsTotal = 0

    oldKey = thisKey
    itemsTotal += float(thisItem)

if oldKey != None:
    print oldKey, "\t", itemsTotal

