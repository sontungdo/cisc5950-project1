import sys

top_n = 5
current_top_n = [] 


for line in sys.stdin:
    count, hour = line.strip().split('\t')
    current_top_n.append((int(count), hour))
    current_top_n.sort(reverse=True)  # Maintain descending order based on count

    # Keep only the top N entries
    current_top_n = current_top_n[:top_n] 

# Output results
for count, hour in current_top_n:
    print(hour, count, sep='\t')