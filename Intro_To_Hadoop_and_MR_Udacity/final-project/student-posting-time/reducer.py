#!/usr/bin/python

import sys

old_key = None
this_key = None
author_hours = [0]*24

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    this_key, hour = data
    if old_key and old_key != this_key:
        #max_hour = author_hours.index(max(author_hours))
        for index, value in enumerate(author_hours):
            if value == max(author_hours):
                print old_key,"\t", index
        author_hours = [0]*24
    author_hours[int(hour)] += 1
    old_key = this_key

if old_key:
    #max_hour = author_hours.index(max(author_hours))
    for index, value in enumerate(author_hours):
        if value == max(author_hours):
            print old_key,"\t", index
    
    
    	
