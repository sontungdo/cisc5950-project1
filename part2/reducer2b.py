#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

cluster_sums = {}
cluster_counts = {}

for line in sys.stdin:
    cluster_id, vector_str = line.strip().split('\t')
    vector = tuple(map(float, vector_str.split(',')))

    cluster_sums.setdefault(cluster_id, [0, 0, 0])
    cluster_counts.setdefault(cluster_id, 0)

    cluster_sums[cluster_id] = [sum(x) for x in zip(cluster_sums[cluster_id], vector)] 
    cluster_counts[cluster_id] += 1

for cluster_id, vector_sum in cluster_sums.items():
    count = cluster_counts[cluster_id]
    new_centroid = tuple(x / count for x in vector_sum)
    print('%s\t%s' % (cluster_id, ','.join(map(str, new_centroid)))) 