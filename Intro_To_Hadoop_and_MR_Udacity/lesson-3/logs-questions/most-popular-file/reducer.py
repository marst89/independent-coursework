#!/usr/bin/python

import sys

hits = 0
max_hits = 0

oldKey = None
max_file = None

for file_name in sys.stdin:
    thisKey = file_name
    if oldKey and oldKey != thisKey:
        if max_hits <= hits:
            max_hits = hits
            max_file = oldKey
            oldKey = thisKey
            hits = 0

    oldKey = thisKey
    hits += 1

print max_file, "\t", max_hits

