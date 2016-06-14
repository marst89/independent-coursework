#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	#Skip file headers
	if line[0] == "id":
		continue

	#Input from forum_node.tsv
	if len(line) == 19:
		hour = line[8][11:13]
		print "{0}\t{1}".format(line[3], hour)