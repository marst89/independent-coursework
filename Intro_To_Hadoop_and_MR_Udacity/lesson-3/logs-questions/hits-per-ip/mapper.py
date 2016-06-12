#!/usr/bin/python

# Format of each line is:
# 10.190.174.142 - - [03/Dec/2011:13:28:10 -0800] "GET /images/filmmediablock/360/Chacha.jpg HTTP/1.1" 200 109379
#
# We want the page name element (part of the get request)

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        host, client_id, username, date, zone, method, page, protocol, code, bytes  = data
        print "{0}".format(host)

