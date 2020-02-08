#!/usr/bin/env python3

import subprocess


WIN_RUN_PISKVORK = ['../piskvork/piskvork.exe', 
                    '-p', 'dist/pbrain-gomoku-ai.exe', '../piskvork/pbrain-pela.exe', 
                    '-rule', '1', '-logpipe', 'log-', 
                    '-logmsg', './ai-messages.log', '-outfile', './game.log']

LOG_FILE = 'game.log'


def check_winner():
    with open(LOG_FILE) as f:
        last = f.readlines()[-1].strip()
        winner = int(last)
        return winner


def main():
    N = 10
    d = {}
    for i in range(N):
        subprocess.run(WIN_RUN_PISKVORK)
        winner = check_winner()
        if winner in d:
            d[winner] += 1
        else:
            d[winner] = 1
        print('{}: {}'.format(i, winner))
    print(d)


if __name__ == '__main__':
    main()