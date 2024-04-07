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
    # Accumulate different names into same categories
    if vehicle_color in ['GR', 'GREY', 'GRY']:
        vehicle_color = 'GRAY'
    elif vehicle_color in ['YELLO', 'YELLOW', 'GLD']:
        vehicle_color = 'GOLD'
    elif vehicle_color in ['RD', 'R']:
        vehicle_color = 'RED'
    elif vehicle_color in ['BL', 'BK', 'BLK']:
        vehicle_color = 'BLACK'
    elif vehicle_color in ['WH']:
        vehicle_color = 'WHITE'

    print('%s\t1' % (vehicle_color))  # Use tab as delimiter
