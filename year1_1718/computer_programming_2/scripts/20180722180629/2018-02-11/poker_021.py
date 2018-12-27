#!/usr/bin/env python3

import sys

poker_rankings = [
    'nothing', 
    'one pair', 
    'two pairs', 
    'three of a kind', 
    'a straight', 
    'a flush', 
    'a full house', 
    'four of a kind', 
    'a straight flush', 
    'a royal flush'
    ]

def probability(sample_space_cardinality, event_set_cardinality):
    """Calculate the probability percentage of an event happening. Assume equally likely events."""
    return event_set_cardinality / sample_space_cardinality * 100 

def main():
    ranking_totals = [0]*10 # indices 0-9 represent a poker hand ranking(0 - nothing, 1 - one pair...), values at an index represent how many hands occurred at that ranking.
    for line in sys.stdin:
        ranking = int(line.rstrip().split(',')[-1])
        ranking_totals[ranking] += 1
    total = sum(ranking_totals) # represents the total number of hands in the given data sample.
    for i in range(10):
        print('The probability of {} is {:.4f}%'.format(poker_rankings[i], probability(total, ranking_totals[i])))

if __name__ == '__main__':
    main()