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
    vehicle_type = fields[6]
    vehicle_year = fields[35]
    # Filter out all missing values
    if vehicle_type == '' or vehicle_year == '' or vehicle_year == '0':
        continue
    feature = vehicle_type + ' ' + vehicle_year 

    print('%s\t1' % (feature))  # Use tab as delimiter
