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