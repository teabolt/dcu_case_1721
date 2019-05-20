#!/usr/bin/env python3

"""Simulate the producer-consumer problem. 
The producer produces information that is consumed by the consumer (both happen concurrently / in parallel). 
The amount of production available (buffer) is assumed to be unbounded.
The amount of production available is simulated using the semaphore synchronisation primitive.
The producer and the consumer are simulated using two threads."""

from __future__ import print_function
import threading
import sys
import time


class ValuedSemaphore(threading.Semaphore):
    """Implement ability to look up a semaphore's current value"""

    def __len__(self):
        return self._value

    def __str__(self):
        s = super().__str__()
        return '({}, value={})'.format(s, len(self))


def process_info(f, info, sleep):
    """Do something with information"""
    while True:
        f(info)
        print(threading.current_thread(), info)
        time.sleep(sleep)


def main():
    """Start the simulation"""
    info = ValuedSemaphore(0) # shared resource representing available information, initially zero
    print(info)
    prod = threading.Thread(target=process_info, args=(lambda x: [x.release() for _ in range(3)], info, 3), name='consumer', daemon=True)
    cons = threading.Thread(target=process_info, args=(lambda x: x.acquire(), info, 2), name='producer', daemon=True)
    # if producer sleeps less than the consumer, information tends to increase, else, information tends to stay at zero
    prod.start()
    cons.start()
    print(threading.active_count(), threading.enumerate())
    while True: # make the program killable by CTRL+C by not blocking the main thread by joins and making child threads daemon (program exits if only daemons are left)
        time.sleep(5)


if __name__ == '__main__':
    main()
