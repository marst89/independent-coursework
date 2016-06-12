#!/usr/bin/python

import sys

items_total = 0
items_count = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisItem = data_mapped

    if oldKey and oldKey != thisKey:
        avg = items_total/float(items_count)
        print oldKey, "\t", avg
        oldKey = thisKey
        items_total = 0
        items_count = 0

    oldKey = thisKey
    items_total += float(thisItem)
    items_count += 1

if oldKey:
    avg = items_total/float(items_count)
    print oldKey, "\t", avg

