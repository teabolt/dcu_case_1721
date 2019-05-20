#!/usr/bin/env python3

import threading


shared = []
wlock = threading.Lock()


def write(idnum):
    global wlock, shared
    for i in range(10):
        wlock.acquire()
        shared.append(idnum)
        print(end='') # momentarily release the GIL
        shared.append(-idnum)
        wlock.release()
        print(end='') # release GIL


def main():
    ws = [threading.Thread(target=write, args=(i,)) for i in range(1, 3)]
    for w in ws:
        w.start()
    for w in ws:
        w.join()
    print(shared)


if __name__ == '__main__':
    main()