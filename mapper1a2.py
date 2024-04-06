import sys

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    print(count, '\t', hour, sep='')