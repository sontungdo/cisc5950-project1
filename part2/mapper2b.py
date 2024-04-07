#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
import csv
import random

def load_centroids(centroids_path):
    centroids = []
    with open(centroids_path, 'r') as f:
        for line in f:
            centroid = tuple(map(float, line.strip().split(',')))
            centroids.append(centroid)
    return centroids

def find_nearest_centroid(vector, centroids):
    min_distance = float('inf')
    nearest_centroid_id = None

    for i, centroid in enumerate(centroids):
        distance = sum((a - b) ** 2 for a, b in zip(vector, centroid))  # Euclidean distance
        if distance < min_distance:
            min_distance = distance
            nearest_centroid_id = i

    return nearest_centroid_id

centroids = load_centroids('centroids.txt')  
header_skipped = False

for line in csv.reader(sys.stdin):
    # Skip header
    if not header_skipped:
        header_skipped = True
        continue
    
    if line[8] == '' or line[11] == '' or line[16] == '':
        continue
    player_name = line[19] 
    shot_dist = float(line[11])
    close_def_dist = float(line[16])
    shot_clock = float(line[8])

    vector = (shot_dist, close_def_dist, shot_clock)
    nearest_centroid_id = find_nearest_centroid(vector, centroids)
    print('%s\t%s' % (nearest_centroid_id, ','.join(map(str, vector)))) 




    
