#!/bin/sh

input_file=$1
num_iter=$2
# Populate random centroids
cat ../../data/nba_small.csv | python generate_centroids.py 
# Start and clean up
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/

# Input preparation
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../data/$input_file /project1/input/

# Question 2b
for i in {1..$2}; 
do
    /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  \
        -input /project1/input/ \
        -output /project1/output \
        -mapper mapper2b.py \
        -reducer reducer2b.py \
        -file mapper2b.py \
        -file reducer2b.py \
        -file centroids.txt 
    # Update centroids for next iteration
    mv /project1/output/part-00000 centroids.txt 
done
# Output and clean up output
/usr/local/hadoop/bin/hdfs dfs -cat /project1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/

# Clean up and stop
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/ 
../../stop.sh