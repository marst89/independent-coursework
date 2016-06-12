#!/usr/bin/python

import sys

count = 0
oldKey = None
nodes_list = []
nodes_ids = ""

for line in sys.stdin: 
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    thisKey, node_id = data
    if oldKey and oldKey != thisKey:
        nodes_list.sort(key=int)
        nodes_ids = ",".join(map(str,nodes_list))
        print "{0}\t{1}\t{2}".format(oldKey, count, nodes_ids)
        oldKey = thisKey
        count = 0
        nodes_list = []

    oldKey = thisKey
    count += 1
    if node_id not in nodes_list:
        nodes_list.append(node_id)

if oldKey:
    nodes_list.sort(key=int)
    nodes_ids = ",".join(map(str,nodes_list))
    print "{0}\t{1}\t{2}".format(oldKey, count, nodes_ids)

