import sys

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    print('%s\t%s' % (count, hour))