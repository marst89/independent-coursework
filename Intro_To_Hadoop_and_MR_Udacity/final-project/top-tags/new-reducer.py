#!/usr/bin/python

import sys


def update_tags(tags, tag_name, num):
    if tags.has_key(tag_name) or len(tags.keys()) < 10:
        tags[tag_name] = num
    else:
        least_used_tag = min(tags, key=tags.get)
        min_value = tags[least_used_tag]
        if num > min_value:
            del tags[least_used_tag]
            tags[tag_name] = num


def reducer():
    tags = {}
    this_tag = None
    old_tag = None
    count = 0

    for line in sys.stdin:
        data = line.strip().split()

        if len(data) != 1:
            continue
        this_tag = data[0]
        if old_tag and old_tag != this_tag:
            update_tags(tags, old_tag, count)
            count = 0

        count += 1
        old_tag = this_tag

    if old_tag:
        update_tags(tags, old_tag, count)

    top10_tags = sorted(tags, key=tags.get, reverse=True)[:10]
    for tag in top10_tags:
        print tag, "\t", tags[tag]

if __name__ == "__main__":
    reducer()
