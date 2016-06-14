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
		if node_type == "question":
			for tag in line[2].split( ):
				print tag