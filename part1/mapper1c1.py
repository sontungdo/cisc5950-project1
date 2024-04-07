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
    violation_precinct = fields[14]
    # Filter out all missing values
    if violation_precinct == '':
        continue

    print('%s\t1' % (violation_precinct))  # Use tab as delimiter
