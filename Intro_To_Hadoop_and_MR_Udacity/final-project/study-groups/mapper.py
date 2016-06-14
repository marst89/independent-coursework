#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    #Skip file headers
    if line[0] == "id":
        continue

    if len(line) == 19:
        node_type = line[5]
        author_id = line[3]
        if node_type == "question":
            identifier = line[0]
        else:
            identifier = line[7]
        print "{0}\t{1}".format(identifier, author_id)

