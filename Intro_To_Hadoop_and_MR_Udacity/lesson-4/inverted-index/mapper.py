#!/usr/bin/python

# Format of each line is:
# 10.190.174.142 - - [03/Dec/2011:13:28:10 -0800] "GET /images/filmmediablock/360/Chacha.jpg HTTP/1.1" 200 109379

import sys
import re
import csv

header_line = True
reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if header_line:
        header_line = False
        continue

    if len(line) == 19:
        node_id = line[0].strip('\"')
        body = re.split(r'[.,!?:;\"\(\)\<\>\[\]#$\=\-\/\s]', line[4])
        for word in body:
            if len(word) >= 1:
                print "{0}\t{1}".format(word.strip().lower(), node_id)

