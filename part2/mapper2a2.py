#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

for line in sys.stdin:
    fields = line.strip().split('\t')
    key = fields[0]
    player_name, defender_name = key[1:-1].split(',')  # Unpack tuple
    hit_rate = float(fields[1])

    print('%s\t%s\t%f' % (player_name, defender_name, hit_rate))