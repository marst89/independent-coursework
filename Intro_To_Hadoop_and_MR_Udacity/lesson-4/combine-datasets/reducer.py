#!/usr/bin/python

import sys

users = {}
nodes = {}

for line in sys.stdin: 
    data = line.strip().split("\t")
    if data[1] == "A":
        user_id, d_type, reputation, gold, silver, bronze = data
        users[user_id] = [reputation, gold, silver, bronze]
    elif data[1] == "B":
        author_id, d_type, title, tagnames, post_id, node_type, parent_id, abs_parent_id, added_at, score = data
        nodes[post_id] = [title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score]

for post_id in nodes:
    title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score = nodes[post_id]
    reputation, gold, silver, bronze = users[author_id]
    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(post_id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, bronze)
