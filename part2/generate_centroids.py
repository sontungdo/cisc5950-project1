import sys
import random
import csv

def generate_random_centroids(data, num_centroids=4):
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    # Find feature ranges
    for shot_dist, close_def_dist, shot_clock in data:
        min_x = min(min_x, shot_dist)
        max_x = max(max_x, shot_dist)
        min_y = min(min_y, close_def_dist) 
        max_y = max(max_y, close_def_dist) 
        min_z = min(min_z, shot_clock)
        max_z = max(max_z, shot_clock)

    centroids = []
    for _ in range(num_centroids):
        centroid = (
            random.uniform(min_x, max_x),
            random.uniform(min_y, max_y),
            random.uniform(min_z, max_z)
        )
        centroids.append(centroid)

    return centroids

data = []
header_skipped = False
for line in csv.reader(sys.stdin):
    # Skip header
    if not header_skipped:
        header_skipped = True
        continue
    
    if line[8] == '' or line[11] == '' or line[16] == '':
        continue
    shot_dist = float(line[11])
    close_def_dist = float(line[16])
    shot_clock = float(line[8])
    data.append((shot_dist, close_def_dist, shot_clock))

centroids = generate_random_centroids(data)

with open('centroids.txt', 'w') as f:
    for centroid in centroids:
        f.write(','.join(map(str, centroid)) + '\n')