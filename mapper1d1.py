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
    vehicle_color = fields[33]
    # Filter out all missing values
    if vehicle_color == '':
        continue

    print('%s\t1' % (vehicle_color))  # Use tab as delimiter
