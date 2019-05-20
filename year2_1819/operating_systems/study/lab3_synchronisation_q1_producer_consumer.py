#!/usr/bin/env python3

from __future__ import print_function

import multiprocessing
import threading
import queue
from random import randint
from time import sleep


def produce(buf, curr):
    while True:
        x = randint(-10, 10)
        buf.put(x)
        print(curr(), x)
        sleep(randint(0, 2))


def consume(buf, curr):
    while True:
        x = buf.get()
        print(curr(), x)
        sleep(randint(0, 3))


def get_queue_repr(q):
    # broken. don't use.
    try:
        queue = q._queue  # threading
    except AttributeError:
        queue = q._buffer # multiprocessing
    return queue
     


def MP():
    print(multiprocessing.cpu_count())
    unbounded_buffer = multiprocessing.Queue()
    producer = multiprocessing.Process(name='producer1', 
        target=produce, args=(unbounded_buffer, multiprocessing.current_process), daemon=True)
    consumer = multiprocessing.Process(name='consumer1', 
        target=consume, args=(unbounded_buffer, multiprocessing.current_process), daemon=True)
    producer.start()
    consumer.start()
    try:
        while True:
            sleep(1024)
    except KeyboardInterrupt:
        print('you done now')


def MT():
    unbounded_buffer = queue.Queue()
    producer = threading.Thread(name='producer1', 
        target=produce, args=(unbounded_buffer, threading.current_thread), daemon=True)
    consumer = threading.Thread(name='consumer1',
        target=consume, args=(unbounded_buffer, threading.current_thread), daemon=True)
    producer.start()
    consumer.start()
    try:
        while True:
            sleep(1024)
    except KeyboardInterrupt:
        print('you done now')


def main():
    MP()
    MT()


if __name__ == '__main__':
    main()