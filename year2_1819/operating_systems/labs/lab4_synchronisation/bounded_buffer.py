#!/usr/bin/env python3

"""Simulate the bounded buffer problem. This is like the producer consumer problem but the buffer (amount of information produced and ready to be consumed) is bounded (has a limit). 
Multiple producers and consumers are simulated by processes and threads within processes.
The buffer is implemented in two ways. In the first way, it is a bounded semaphore (counter with an upper limit). In the second way, it is a shared queue."""

import multiprocessing # do not import as 'mp' as want to make the code more readable
# import multiprocessing.managers
import threading
import os
# import queue
import time
import random


# class ValuedBoundedSemaphore(multiprocessing.managers.SyncManager.BoundedSemaphore):

#     def __len__(self):
#         return self._getvalue()

#     def __str__(self):
#         s = super().__str__()
#         return 'str={}, count={}'.format(s, len(self))

    # def acquire(self, blocking=True, timeout=None):
    #     retval = super().acquire(blocking=blocking, timeout=timeout)
    #     return 'Return value={}, count={}'.format(retval, len(self))

    # def release(self):
    #     retval = super().release()
    #     return 'Return value={}, count={}'.format(retval, len(self))


def affect_buffer(sleep_delay, shared, bound_method, *args):
    while True:
        if len(args) > 1 and callable(args[0]):
            method_args = (args[0](*args[1:]), )
        else:
            method_args = args
        retval = bound_method(*method_args)
        print('{}: Process "{}", Thread "{}": did "{}" with args "{}" evaluated as "{}" on "{}" with state "{}" resulting in "{}"'.format(
            time.ctime(), multiprocessing.current_process(), threading.current_thread(), bound_method.__name__, args, method_args, shared.__class__, shared, retval), end='\n\n')
        time.sleep(sleep_delay)


def effect_workers(worker_number, *args):
    workers = [threading.Thread(name="(proc={}, threadnum={})".format(os.getpid(), i), target=affect_buffer, args=args) for i in range(worker_number)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()


def main():
    """Start the simulation"""
    N = 10 # buffer size
    bounded_buffer = multiprocessing.Queue(N) # use a process-specific shared queue (else multiprocessing can't pickle the standard thread shared queue)
    bounded_semaphore = multiprocessing.Manager().BoundedSemaphore(N) # indicate the state of the queue at various points in time (may get out of sync with the queue) (need to use the manager to not get a pickle error)

    # queue based solution
    # producer = multiprocessing.Process(name="producer", target=effect_workers, args=(5, 2, bounded_buffer, bounded_buffer.put, random.randint, -10, 10), daemon=True)
    # consumer = multiprocessing.Process(name="consumer", target=effect_workers, args=(5, 3, bounded_buffer, bounded_buffer.get), daemon=True)

    # semaphore based solution
    producer = multiprocessing.Process(name="producer", target=effect_workers, args=(5, 2, bounded_semaphore, bounded_semaphore.release,), daemon=True)   
    consumer = multiprocessing.Process(name="consumer", target=effect_workers, args=(5, 3, bounded_semaphore, bounded_semaphore.acquire,), daemon=True)
    producer.start()
    consumer.start()
    try:
        while True: # wait for a keyboard interrupt
            time.sleep(5)
    except KeyboardInterrupt:
        print('Exiting...')


if __name__ == '__main__':
    main()