#!/bin/sh

# Start and clean up
../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/

# Input preparation
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../data/rows_small.csv /project1/input/

# Question 1a
# MapReduce Round 1
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper1a1.py -mapper mapper1a1.py \
-file reducer1a1.py -reducer reducer1a1.py \
-input /project1/input/* -output /project1/tmp/
# MapReduce Round 2
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/ 
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper1a2.py -mapper mapper1a2.py \
-file reducer1a2.py -reducer reducer1a2.py \
-input /project1/tmp/* -output /project1/output/
# Output
/usr/local/hadoop/bin/hdfs dfs -cat /project1/output/part-00000



# Clean up and stop
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/ 
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/tmp/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/
../stop.sh
