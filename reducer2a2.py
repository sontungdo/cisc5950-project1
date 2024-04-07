#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

current_player = None
min_hit_rate = 1
most_unwanted_defender = None

for line in sys.stdin:
    fields = line.strip().split('\t')
    player_name = fields[0]
    defender_name = fields[1]
    hit_rate = float(fields[2])

    if current_player == player_name:
        if hit_rate < min_hit_rate:
            min_hit_rate = hit_rate
            most_unwanted_defender = defender_name
    else:
        if current_player:  # Not the first player
            print('%s\t%s\t%f' % (current_player, most_unwanted_defender, min_hit_rate))

        current_player = player_name
        min_hit_rate = hit_rate
        most_unwanted_defender = defender_name

# Output the last player
if current_player:
    print('%s\t%s\t%f' % (current_player, most_unwanted_defender, min_hit_rate))
