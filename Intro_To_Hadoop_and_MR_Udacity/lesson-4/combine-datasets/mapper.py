#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	#Skip files headers
	if line[0] == "user_ptr_id" or line[0] == "id":
		continue

	#Input from forum_node.tsv
	if len(line) == 19:
		post_id, title, tagnames, usr_id, _, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(usr_id, "B", title, tagnames, post_id, node_type, parent_id, abs_parent_id, added_at, score)
	elif len(line) == 5:
		usr_id, reputation, gold, silver, bronze = line
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(usr_id, "A", reputation, gold, silver, bronze)

