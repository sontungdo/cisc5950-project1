#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

header_skipped = False

for line in sys.stdin:
    # Skip header
    if not header_skipped:
        header_skipped = True
        continue
    
    fields = line.strip().split(',')
    violation_time = fields[19]
    # Filter out all missing values
    if violation_time == '':
        continue
    hour = violation_time[0:2] + violation_time[4] # get hour, remove minute

    print('%s\t1' % (hour))  # Use tab as delimiter
