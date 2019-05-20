#!/usr/bin/env python3

"""
Readers-writers problem. 
One shared record, multiple reader/writer nodes.
Allow multiple readers to read, but only one writer to write.
Readers only read, don't do updates.
Writers can read AND write.
"""


import threading
import time
import random


class Reader(threading.Thread):
    def __init__(self, reader_id, file, barrier=None):
        super().__init__(
            group=None, target=None, args=(), kwargs={},
            name='reader-%d' % reader_id, 
            daemon=True,
        )
        self.file = file
        self.barrier = barrier

    def run(self):
        print('Starting reader:', self.name)
        if self.barrier is not None:
            self.barrier.wait()
        self.read()

    def read(self):
        f = open(self.file)
        while True:
            for line in f:
                print(self.name, 'read:', repr(line))
                delay = random.random()*4
                time.sleep(delay)
            f.seek(0)
            print(self.name, 'reset pointer')


class Writer(threading.Thread):
    def __init__(self, writer_id, file, write_lock, barrier=None):
        super().__init__(
            group=None, target=None, args=(), kwargs={},
            name='writer-%d' % writer_id, 
            daemon=True,
        )
        self.file = file
        self.write_lock = write_lock
        self.barrier = barrier

    def run(self):
        print('Starting writer:', self.name)
        if self.barrier is not None:
            self.barrier.wait()
        self.write()

    def write(self):
        f = open(self.file, 'a') 
        # open file to append to (don't use 'w' as that will overwrite the file)
        # can not read from the file however!
        while True:
            line = self.name + '' + chr(random.randint(ord('A'), ord('z'))) + '\n'
            with self.write_lock:
                print(self.name, 'writing:', repr(line))
                f.write(line)
                f.flush() # write out the line
            delay = random.random()*4
            time.sleep(delay)


# Problem:
# Concurrent reads/writes to a file object are already handled by Python / kernel reader-writer locks (so this problem is already solved)
# Also, Python has Global Interpreter Lock, so can't really experience the problem? 
# (but these read/write operations are IO-bound, so GIL is released before the IO call!?)
# but thread safety on files is questionnable
# better to use a shared queue

# Condition - only one writer at a time
# Some solutions:
# - readers don't wait unless writer has writing permission
# - writer writes once ready ASAP


# update: using a buffer / list is fine over a file

def main():
    dataset = 'dataset.txt'
    N_readers = 5
    N_writers = 3
    reader_barrier = threading.Barrier(N_readers)
    writer_barrier = threading.Barrier(N_writers)
    write_lock = threading.Lock()
    readers = [Reader(i, dataset, reader_barrier) for i in range(N_readers)]
    writers = [Writer(i, dataset, write_lock, writer_barrier) for i in range(N_writers)]
    for reader in readers:
        reader.start()
    for writer in writers:
        writer.start()
    while True:
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            raise SystemExit('Quitting...')


if __name__ == '__main__':
    main()