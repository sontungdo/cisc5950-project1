#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

current_key = None
shot_count = 0
hit_count = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    
    count, shot_result = value[1:-1].split(',')  # Unpack tuple
    shot_result = shot_result[2:-1]

    if current_key == key:
        shot_count += 1
        if shot_result == 'made':
            hit_count += 1
    else:
        if current_key:  # Not the first key
            hit_rate = hit_count / shot_count
            print('%s\t%f' % (current_key, hit_rate))

        current_key = key
        shot_count = 1
        hit_count = 1 if shot_result == 'made' else 0

if current_key:
    hit_rate = hit_count / shot_count
    print('%s\t%f' % (current_key, hit_rate)) 