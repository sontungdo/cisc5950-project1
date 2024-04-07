#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv

header_skipped = False

for line in csv.reader(sys.stdin):
    # Skip header
    if not header_skipped:
        header_skipped = True
        continue
    
    defender_name = line[14].strip().split(',')
    if len(defender_name) < 2:
        defender_name = defender_name[0].strip()
    else:
        defender_name = defender_name[1].strip() + ' ' + defender_name[0].strip()
    player_name = line[19]
    shot_result = line[13]


    if shot_result in ('made', 'missed'):
        key = (player_name, defender_name)
        value = (1, shot_result)  # Represent outcome as a tuple
        print('%s\t%s' % (key, value))