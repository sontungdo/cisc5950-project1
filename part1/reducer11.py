#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

current_feature = None
current_count = 0

for line in sys.stdin:
    feature, count = line.strip().split('\t')
    count = int(count)

    if current_feature == feature:
        current_count += count
    else:
        # Output current feature and reset for next feature
        if current_feature: 
            print('%s\t%s' % (current_feature, current_count))
        current_feature = feature
        current_count = count

# Output the last feature
if current_feature: 
    print('%s\t%s' % (current_feature, current_count))