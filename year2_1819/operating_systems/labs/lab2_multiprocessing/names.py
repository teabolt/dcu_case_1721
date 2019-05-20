#!/usr/bin/env python3

import multiprocessing as mp
import time


def greet(q, l, N):
    for _ in range(N):
        l.acquire()
        print('Waiting for name ...')
        l.release()
        name = q.get()
        l.acquire()
        print('Greetings to {} from {}'.format(name, mp.current_process().name))
        l.release()


def sendNames():
    q = mp.Queue()
    l = mp.Lock()
    N = 5

    p = mp.Process(target=greet, args=(q, l, N), name='greeter')
    p.start()
    for _ in range(N):
        l.acquire()
        q.put(input('Enter a name: '))
        l.release()
        time.sleep(0.5)
        # p.join()


def main():
    sendNames()


if __name__ == '__main__':
    main()