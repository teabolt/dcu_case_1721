#!/usr/bin/env python3

import os
import sys
import re

# from brain_random import BrainRandom
from brain_minimax import BrainMinimax


# use regex matching for commands
commands_re = {
    'start': re.compile(r'^START \d+$'),
    'begin': re.compile(r'^BEGIN$'),
    'turn': re.compile(r'^TURN \d+,\d+$'),
    'board': re.compile(r'^BOARD$'),
    'boarddata': re.compile(r'^\d+,\d+,[1-3]$'),
    'boarddone': re.compile(r'^DONE$'),
    'info': re.compile(r'^INFO \S+ \S+$'),
    'about': re.compile(r'^ABOUT$'),
    'end': re.compile(r'^END$'),
}


def find_match(line):
    for comm in commands_re:
        if commands_re[comm].match(line):
            return comm


class GomokuAiWrapper(object):

    def __init__(self, brain_cls, logfile, about):
        self.brain_cls = brain_cls
        self.about = about

        with open(logfile, 'w') as f:
            pass
        self.logfile = open(logfile, 'a')

        self.got_start = False
        self.got_board = False
        self.got_begin = False
        self.brain = None
        self.err = 0


    def stop(self):
        self.logfile.close()

    def start(self):
        keep_going = True
        self.log('Starting')
        while keep_going:
            line = self.read()
            keep_going = self.exec(line)
        self.log('Stopping')

    def exec(self, line):
        comm = find_match(line)
        if comm is None:
            self.log('[ERR] Line not understood: ' + line)
            self.err = 84
            return False
        else:
            handler = getattr(self, 'handle_' + comm)
            return handler(line)
            # try:
            #     return handler(line)
            # except BaseException as e:
            #     self.log('Exception ' + str(e))
            #     self.err = 84
            #     return False

    def write(self, line):
        self.log('[LOG] writing line: ' + line)
        print(line, flush=True)
        # sys.stdout.write(s + '\n')
        # sys.stdout.flush()
        # os.fsync(sys.stdout.fileno())

    def read(self):
        # line = input()
        line = sys.stdin.readline()
        line = line.strip()
        self.log('[LOG] read line: ' + line)
        return line

    def log(self, line):
        print(line, file=self.logfile, flush=True)

    def handle_start(self, line):
        self.log('Handling START')
        if self.got_start:
            self.log('Unexpected START')
            self.err = 84
            return False
        else:
            self.got_start = True
            _, board_size = line.split()
            board_size = int(board_size)
            try:
                # initialize brain
                self.brain = self.brain_cls(board_size)
            except ValueError:
                self.write('ERROR unsupported size')
                self.err = 84
                return False
            else:
                self.write('OK')
                return True

    def handle_turn(self, line):
        self.log('Handling TURN')
        if not self.got_start:
            self.log('Unexpected TURN')
            self.err = 84
            return False
        else:
            _, coordinates = line.split()
            x, y = map(int, coordinates.split(','))
            self.log('Got turn coordinates: {}, {}'.format(x, y))
            self.brain.update_state(2, x, y)
            i, j = self.brain.make_move()
            self.log('[DEBUG] AI puts stone on {} and {}'.format(i, j))
            self.write('{},{}'.format(i, j))
            return True

    def handle_begin(self, line):
        self.log('Handling BEGIN')
        if self.got_begin or (not self.got_start):
            self.log('Unexpected BEGIN')
            self.err = 84
            return False
        else:
            self.got_begin = True
            i, j = self.brain.make_move()
            self.write('{},{}'.format(i, j))
            return True

    def handle_board(self, line):
        self.log('Handling BOARD')
        if self.got_board:
            self.log('Unexpected BOARD')
            self.err = 84
            return False
        else:
            self.got_board = True
            return True

    def handle_boarddata(self, line):
        self.log('Handling BOARDDATA')
        if not self.got_board:
            self.log('Unexpected BOARDDATA')
            self.err = 84
            return False
        else:
            x, y, field = map(int, line.split(','))
            self.log('Got boarddata: {},{} for {}'.format(x, y, field))
            self.brain.update_state(field-1, x, y)
            return True

    def handle_boarddone(self, line):
        self.log('Handling BOARDDONE')
        if not self.got_board:
            self.log('Unexpected BOARDDONE')
            self.err = 84
            return False
        else:
            self.got_board = False
            return True

    def handle_info(self, line):
        self.log('Handling INFO')
        _, key, value = line.split()
        self.log('Got info: {}: {}'.format(key, value))
        return True

    def handle_about(self, line):
        self.log('Handling ABOUT')
        self.write(self.about)
        return True

    def handle_end(self, line):
        self.log('Handling END')
        return False


def main():
    brain_cls = BrainMinimax  # actual AI to use
    ai = GomokuAiWrapper(brain_cls, 'ai-debug.log', 'name="tomas_ai", version="1.0", author="Tomas", country="Fr"')
    # DEBUG
    # ai.handle_start('START 19')

    # begin loop
    ai.start()
    
    # DEBUG
    if ai.brain:
        ai.log('DUMPING BRAIN STATE')
        ai.log(str(ai.brain.board))

    # exit
    ai.stop()
    sys.exit(ai.err)


if __name__ == '__main__':
    main()
