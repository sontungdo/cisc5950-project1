# Part 1
Run test1.sh with a file name argument

The system aims to efficiently analyze a large dataset of parking violations in NYC using MapReduce. One thing in common between all data analysis questions of this part is that they all follow the same formula: which specific type of a feature has the highest count of tickets. Because of this, all 4 questions can be addressed using the same strategy of 2 rounds of MapReduce as followed:
-	Mapper 1 round 1: Read the dataset then output pairs of (feature, 1)
-	Reducer 1 round 1: Accumulate the count for every feature and output (feature, count)
-	Mapper 1 round 2: Reverse the output into (count, feature)
-	Reducer 1 round 2: Maintain a list of top 5 counts and process each line. Each line with count big enough for top 5 would push the current top 5 out of the list. At the end, output 5 pairs of (hour, count) with the 5 biggest counts. I choose to output top 5 instead of just top 1.
Only mapper 1 round 1 is required to have different versions for each question, while all other mappers and reducers can be shared between every case. Some specific changes are required in mapper 1 round 1 to process different kinds of data:
(My MapReduce keeps getting error on the full dataset, so I can only run them on a subset with the first 1000 rows of the original data)
-	Question a: mapper reads column index 19 to get violation time, then remove minute to get only the hour.
-	Question b: mapper reads columns index 6 and 35 to get vehicle types and years made, then concatenate them together.
-	Question c: mapper reads column index 14 to get the violation police precincts, a good estimate of location.
-	Question d: mapper reads column index 33 to get the car colors and merge similar color names together.

