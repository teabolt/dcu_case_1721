#!/usr/bin/env python3

import threading
import time
import random
import statistics


class Philosopher(threading.Thread):
    def __init__(self, name, idnum, forkl, forkr, stopevent):
        threading.Thread.__init__(self)
        self.name = name
        self.idnum = idnum
        self.forkl = forkl
        self.forkr = forkr
        self.stopevent = stopevent
        self.weight = 0

    def run(self):
        global waitforall
        waitforall.wait()
        while not self.stopevent.is_set():
            self.think()
            self.dine()

    def think(self):
        print(self.name, 'is thinking.')

    def dining(self):
        print(self.name, 'is dining')
        self.weight += 1

    def dine_naive(self):
        # this deadlocks
        self.forkl.acquire()
        print(self.name, 'took fork left')
        self.forkr.acquire()
        print(self.name, 'took fork right')
        self.dining()
        self.forkl.release()
        print(self.name, 'released fork left')
        self.forkr.release()
        print(self.name, 'released fork right')

    def dine_csection_with(self):
        # this deadlocks too
        with self.forkl, self.forkr:
            self.dining()

    def dine_sleep(self):
        # this works sometimes
        self.dine_naive()
        time.sleep(random.random())

    def dine_csection(self):
        # this works but can be improved by having multiple locks on different sides of the table
        global cantake 
        with cantake:
            self.forkl.acquire()
            self.forkr.acquire()
            self.dining()
            self.forkl.release()
            self.forkr.release()

    def dine_asymmetric(self):
        if self.idnum % 2 == 0: 
            # even
            self.forkl.acquire()
            self.forkr.acquire()
        else:
            # odd
            self.forkr.acquire()
            self.forkl.acquire()
        self.dining()
        self.forkl.release()
        self.forkr.release()

    def dine_nonblocking(self):
        self.forkl.acquire()
        taken = self.forkr.acquire(False)
        if not taken:
            # if the other fork is taken, drop your current fork and exit
            self.forkl.release()
            return
        else:
            self.dining()
            self.forkl.release()
            self.forkr.release()

    def dine(self):
        print(self.name, 'is hungry.')
        # these don't work:
        # self.dine_naive()
        # self.dine_csection_with()

        # these work:
        # self.dine_csection()
        # self.dine_sleep() # <- this works badly and sometimes doesn't stop

        # these two seem to be the best:
        # self.dine_asymmetric()
        self.dine_nonblocking()
        print(self.name, 'finished dining.')


cantake = threading.Lock() # create a critical section for taking the forks
waitforall = threading.Barrier(5) # wait until all threads are ready to run (so that the first philosophers don't get a head start)


def main():
    forks = [threading.Lock() for i in range(5)]
    stopevent = threading.Event()
    philosophers = [Philosopher('Philosopher %i' % i, i, forks[i%5],
    forks[(i+1)%5], stopevent) for i in range(5)]
    for p in philosophers:
        p.start()
        # time.sleep(10) # <- this makes the first philosophers eat the most (if no barrier is used)
    time.sleep(5) # run test for a number of seconds
    print('[Setting Stop-Event.]')
    stopevent.set()
    print('[Waiting for Philosophers to stop...'),
    for p in philosophers:
        p.join()
        print('Done.')
    world_weights = [p.weight for p in philosophers]
    print('How much each ate:', world_weights)
    print('Max:', max(world_weights))
    print('Standard deviation:', statistics.pstdev(world_weights))


if __name__ == '__main__':
    main()