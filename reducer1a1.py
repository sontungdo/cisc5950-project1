#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

current_hour = None
current_count = 0

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    count = int(count)

    if current_hour == hour:
        current_count += count
    else:
        if current_hour:  # Not the first hour
            print('%s\t%s' % (current_hour, current_count))
        current_hour = hour
        current_count = count

# Output the last hour
if current_hour: 
    print('%s\t%s' % (current_hour, current_count))