#!/usr/bin/env python3

import sys

def to_seconds(x):
    mins, secs = x.split(':')
    return int(mins)*60 + int(secs)

def get_time(t):
    return to_seconds(t[1])

def main():
    PBs = {}
    for results in sys.stdin:
        runner = results.rstrip().split()
        name, times = runner[0], runner[1:]
        try:
            best_time = min(times, key=to_seconds)
        except ValueError:
            continue
        PBs[name] = best_time

    season_best = min(PBs.items(), key=get_time)
    b_name, b_time = season_best[0], season_best[1]

    print('{} : {}'.format(b_name, b_time))

if __name__ == '__main__':
    main()