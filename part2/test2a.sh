#!/bin/sh

input_file=$1

# Start and clean up
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/

# Input preparation
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/$input_file /project1/input/

# Question 2a
# MapReduce Round 1
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file /mapreduce-test/cisc5950-project1/part2/mapper2a1.py -mapper /mapreduce-test/cisc5950-project1/part2/mapper2a1.py \
-file /mapreduce-test/cisc5950-project1/part2/reducer2a1.py -reducer /mapreduce-test/cisc5950-project1/part2/reducer2a1.py \
-input /project1/input/* -output /project1/tmp/
# MapReduce Round 2
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file /mapreduce-test/cisc5950-project1/part2/mapper2a2.py -mapper /mapreduce-test/cisc5950-project1/part2/mapper2a2.py \
-file /mapreduce-test/cisc5950-project1/part2/reducer2a2.py -reducer /mapreduce-test/cisc5950-project1/part2/reducer2a2.py \
-input /project1/tmp/* -output /project1/output/
# Output and clean up output
/usr/local/hadoop/bin/hdfs dfs -cat /project1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/tmp/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/

# Clean up and stop
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/ 
../../stop.sh
