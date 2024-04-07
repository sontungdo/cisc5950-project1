# Part 2
Run test2a.sh for first part
This system aims to measure performance analytics of NBA players using MapReduce. 
Question 2a: measure hit_rate of a player A when facing player B. A lower hit_rate means player A fearing defender B more. This implementation uses 2 rounds of MapReduce:
-	Mapper 1 round 1: Read the dataset then output pairs of ((player name, defender name), (1, shot result))
-	Reducer 1 round 1: Accumulate the count for every shot, calculate the hit rate, and output ((player name, defender name), hit rate)
-	Mapper 1 round 2: Output ((player name, defender name), hit rate)
-	Reducer 1 round 2: Keep track of minimum hit rate of every defender for each player, output (player, most unwanted defender, minimum hit rate)

---
Run test2b.sh for second part
This part couldn't work on Hadoop. I only managed to run it for 1 iteration locally
-	Mapper 2b: Read inputs at specified columns to get player names and the 3 measures needed for the matrix, load existing 4 centroids, find the nearest centroids for each matrix, then output (player_name, centroid_id, matrix)
-	Reducer 2b: Accumulate results from mapper, train the K-means clustering model by moving the centroids to the center of their regions, and output the new 4 centroids.
Additionally, before the mapper-reducer loop can be run, I have a script random_centroid.sh that can populate centroids.txt with 4 random centroids with reasonable random values (within range for each feature). This feature is already included at the start of test2b.sh script when run in a Hadoop cluster.
