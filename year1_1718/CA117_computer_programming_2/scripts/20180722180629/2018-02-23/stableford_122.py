#!/usr/bin/env python3

import sys

no_of_holes = 18

def get_free_strokes(handicap):
    """Return a list of free strokes for holes with indexes 1-18(list indices 0-17)."""

    # Each handicap point gives 1 free stroke for a hole with some index. The index order goes from 1 to 18, then wraps around(modulo).
    fully_free = handicap // no_of_holes
    partly_free = handicap % no_of_holes

    free_strokes = [fully_free]*no_of_holes # efficiently initialize the list of free strokes, covering all holes.
    for i in range(partly_free): # add the remaining free strokes to certain holes.
        free_strokes[i] += 1

    return free_strokes

def get_points(par_score):
    """Given a score to par at a hole, return the corresponding points that that par score gives."""
    if par_score < 3:
        return abs(par_score-2)
    else:
        return 0

def int_x(n):
    """A custom 'int' constructor, returning 100 for 'X' and an attempted integer for everything else."""
    if n == 'X':
        return 100
    else:
        return int(n)

def index_to_1(a):
    """Returns the second element(index one) of an iterable. Usable as a 'key' function."""
    return a[1]

def main():
    # holes with *numbers* 1-18 are represented by list indices 0-17.
    holes = [h for h in range(no_of_holes)] # phoney list of holes.
    hole_pars = [int(par) for par in sys.stdin.readline().split()]
    hole_indexes = [int(index) for index in sys.stdin.readline().split()]

    results = []
    disqualified = []
    for line in sys.stdin: # read each player
        try:
            player_details = line.rstrip().split()
            name = ' '.join(player_details[:-19])
            handicap = int(player_details[-19])
            gross_strokes = [int_x(stroke) for stroke in player_details[-18:]]
            # 'X' stroke values(to be ignored) obtain the magic number 100, which will contribute nothing to the stableford score when all calculations are done.

            free_strokes = get_free_strokes(handicap)
            net_strokes = gross_strokes # temporary initialization
            for i in range(len(gross_strokes)):
                net_strokes[i] = gross_strokes[i] - free_strokes[hole_indexes[i]-1] 
                # list indices 0-17 represent hole indexes 1-18(offset by 1)

            scores_to_par = [0]*no_of_holes
            for i in range(no_of_holes):
                scores_to_par[i] = net_strokes[i] - hole_pars[i]

            points = [0]*no_of_holes
            for i in range(no_of_holes):
                points[i] = get_points(scores_to_par[i])

            stableford_score = sum(points)
            results.append((name, stableford_score))
        except ValueError:
            disqualified.append(name)

    sorted_results = sorted(results, key=index_to_1, reverse=True)
    names = [res[0] for res in results] + disqualified # names of all participants
    scores_s = [str(res[1]) for res in results]

    longest_name = max(names, key=len)
    if scores_s:
        longest_number = max(scores_s, key=len) # assume stableford scores are less than 100(3 digits), but they can  be either 1 or 2 digits long.

    for res in sorted_results:
        print('{:>{}} : {:>{}}'.format(res[0], len(longest_name), res[1], len(longest_number)))
    for dis in disqualified:
        print('{:>{}} : Disqualified'.format(dis, len(longest_name)))

if __name__ == '__main__':
    main()