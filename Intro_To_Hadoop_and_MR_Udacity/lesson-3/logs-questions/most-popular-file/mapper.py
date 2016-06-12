#!/usr/bin/python

# Format of each line is:
# 10.190.174.142 - - [03/Dec/2011:13:28:10 -0800] "GET /images/filmmediablock/360/Chacha.jpg HTTP/1.1" 200 109379
#
# We want the file (part of the url of the get request)

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        host, client_id, username, date, zone, method, page, protocol, code, num_bytes = data
    file_name = re.match(r'(^http://www.the-associates.co.uk)(.*)', page, re.M | re.I)
    if file:
        print "{0}".format(file_name.group(2))
    else:
        print "{0}".format(page)
