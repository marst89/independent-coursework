#!/usr/bin/python

import sys

hits = 0
oldKey = None

for page in sys.stdin:
    thisKey = page
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hits
        oldKey = thisKey
        hits = 0

    oldKey = thisKey
    hits += 1

if oldKey != None:
    print oldKey, "\t", hits

