#!/usr/bin/python

import sys

students = []
this_forum = None
old_forum = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue
    this_forum, student_id = data
    if old_forum and old_forum != this_forum:
        print "{0}\t{1}".format(old_forum, students)
        students = []

    students.append(student_id)
    old_forum = this_forum

if old_forum:
    print "{0}\t{1}".format(old_forum, students)

