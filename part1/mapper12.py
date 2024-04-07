#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

for line in sys.stdin:
    feature, count = line.strip().split('\t')
    print('%s\t%s' % (count, feature)) # reverse key-value