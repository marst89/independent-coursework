#!/usr/bin/python

import sys

sales_per_weekday = [0]*7

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    weekday, sales = data_mapped
    sales_per_weekday[int(weekday)] += float(sales)

for weekday, total_sales in enumerate(sales_per_weekday):
    print "{0}\t{1}".format(weekday, total_sales)

