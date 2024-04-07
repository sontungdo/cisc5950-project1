#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

top_n = 5
current_top_n = [] 


for line in sys.stdin:
    count, feature = line.strip().split('\t')
    current_top_n.append((int(count), feature))
    current_top_n.sort(reverse=True)  # Maintain descending order based on count
    current_top_n = current_top_n[:top_n] # Keep only the top N entries

# Output results
for count, feature in current_top_n:
    print('%s\t%s' % (feature, count))