#!/usr/bin/env python3

"""Simulate the dining philosophers problem. In it, five philosophers sit side to side at a circular table. There are five plates and five chopsticks. At the centre there is rice. For a philosopher to eat, he or she needs *two* chopsticks. The problem is to synchronise the picking up and placing down of chopsticks so that all philosophers eat and none end up starving. 
In this simulation, philosophers are modelled as threads. Chopsticks are modelled as a bounded semaphore.
"""

import threading
import time


class ChopstickSemaphore(threading.BoundedSemaphore):

    def __len__(self):
        return self._value

    def acquire(self, blocking=True, timeout=None):
        a = super().acquire(blocking=blocking, timeout=timeout)
        b = super().acquire(blocking=blocking, timeout=timeout)
        return a and b

    def release(self):
        a = super().release()
        b = super().release()
        return a and b


class Philosopher(threading.Thread):

    def __init__(self, chopsticks, eating_delay, name=None, daemon=None):
        threading.Thread.__init__(self, name=name, daemon=daemon)
        self.satisfaction = 0
        self.chopsticks = chopsticks
        self.delay = eating_delay

    def run(self):
        self.eat()

    def eat(self):
        while True:
            self.chopsticks.acquire()
            self.satisfaction += 1
            print(time.ctime(), threading.current_thread(), self.satisfaction, sep=', ')
            self.chopsticks.release()
            time.sleep(self.delay)

    def get_satisfaction(self):
        return self.satisfaction


def main():
    Np = 5
    Nc = 5
    chopsticks = ChopstickSemaphore(Nc)
    philosophers = [Philosopher(chopsticks, 0.5, name='philosopher={}'.format(i), daemon=True) for i in range(Np)]
    # changing the delay of each philosopher (or keeping it equal changes the results)
    for philosopher in philosophers:
        philosopher.start()
    try:
        while True:
            print(len(chopsticks))
            time.sleep(5)
    except KeyboardInterrupt:
        print([philosopher.get_satisfaction() for philosopher in philosophers])


if __name__ == '__main__':
    main()
