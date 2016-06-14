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
			rec_id = line[0]
		elif node_type == "answer":
			rec_id = line[7]
		print "{0}\t{1}\t{2}".format(rec_id, node_type, len(line[4]))
