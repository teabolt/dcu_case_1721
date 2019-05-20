#!/usr/bin/env python3

import multiprocessing as mp


def dig(lock, hole):
    lock.acquire()
    print("Hiddy-ho!  I'm worker {} and today I have to dig hole {}".format(mp.current_process().name, hole))
    lock.release()


def assignDiggers(holes, diggers):
    lock = mp.Lock()
    for digger, hole in zip(diggers, holes):
        mp.Process(target=dig, args=(lock, hole), name=digger).start()


def main():
    assignDiggers([i for i in range(10)], [chr(i) for i in range(ord('A'), ord('K'))])


if __name__ == '__main__':
    main()