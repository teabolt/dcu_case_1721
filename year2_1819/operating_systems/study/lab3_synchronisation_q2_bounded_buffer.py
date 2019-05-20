#!/usr/bin/env python3

from __future__ import print_function
import multiprocessing
import threading
from time import sleep
from random import randint


class ProducerProcess(multiprocessing.process.BaseProcess):
    def __init__(self):
        super().__init__(name='producer', daemon=True)

    def __call__(self, buff, delay):
        self.start()
        self._buff = buff
        while True:
            x = randint(-20, 20)
            buff.put(x)
            print('producer', x)
            sleep(delay)


class ConsumerProcess(multiprocessing.process.BaseProcess):
    def __init__(self):
        super().__init__(name='consumer', daemon=True)

    def __call__(self, buff, delay):
        self.start()
        self._buff = buff
        while True:
            x = buff.get()
            print('consumer', x)
            sleep(delay)


def producer_consumer(queue, producer, consumer):
    producer(queue, 2)
    consumer(queue, 1)
    while True:
        sleep(1024)


def MP():
    bound = 10
    queue = multiprocessing.Queue(bound)
    producer = ProducerProcess()
    consumer = ConsumerProcess()
    producer_consumer(queue, producer, consumer)

def main():
    MP()
    # MT()


if __name__ == '__main__':
    main()