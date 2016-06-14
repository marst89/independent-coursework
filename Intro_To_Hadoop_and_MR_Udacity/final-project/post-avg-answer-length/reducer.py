#!/usr/bin/python

import sys

old_key = None
this_key = None
total_body_len = 0
avg_body = 0
this_len = 0
ans_num = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
        continue

    this_key, node_type, body_len = data
    if old_key and old_key != this_key:
        if ans_num == 0:
            print "{0}\t{1}\t{2}".format(old_key, this_len, 0)
        else:
            avg_ans_len = total_body_len/float(ans_num)
            print "{0}\t{1}\t{2}".format(old_key, this_len, avg_ans_len)
            total_body_len = 0
            ans_num = 0
            this_len = 0

    old_key = this_key
    if node_type == "question":
        this_len = body_len
    elif node_type == "answer":
        ans_num += 1
        total_body_len += float(body_len)

if old_key:
    if ans_num == 0:
        print "{0}\t{1}\t{2}".format(old_key, this_len, 0)
    else:
        avg_ans_len = total_body_len/float(ans_num)
        print "{0}\t{1}\t{2}".format(old_key, this_len, avg_ans_len)