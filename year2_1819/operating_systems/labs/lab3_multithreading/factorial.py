#!/usr/bin/env python3

from math import factorial
import threading
import queue
import time


def fac(N):
    if N < 0:
        return -1
    elif N == 0:
        return 1    # 0! = 1
    else:
        return N*fac(N-1)


def ST(nums):
    results = []
    for num in nums:
        results.append(factorial(num))
    return results


def get_factorial(N, result_queue):
    print(threading.current_thread(), 'started for', N, time.ctime())
    result = factorial(N)
    result_queue.put((N, result))
    print(threading.current_thread(), 'ended for', N, time.ctime())


def write(result_queue, required_writes, out='output.txt'):
    writes = 0
    while writes < required_writes:
        result = result_queue.get()
        n, n_fac = result
        print(threading.current_thread(), 'start write for', n, time.ctime())
        with open('output.txt', 'w') as f:
            f.write(str('{} {}'.format(n, n_fac)))
            f.write('\n')
        print(threading.current_thread(), 'end write for', n, time.ctime())
        writes += 1


def MT(nums):
    result_queue = queue.Queue()
    fac_threads = [threading.Thread(target=get_factorial, args=(num, result_queue)) for num in nums]
    # writer_thread = threading.Thread(target=write, args=(result_queue, 3))
    # writer_thread.start()
    for th in fac_threads:
        th.start()
    results = [result_queue.get() for num in nums]
    # writer_thread.join()
    return results


def main():
    print('Program start', time.ctime())
    nums = [10**5, 2*10**5, 3*10**5]
    # results = ST(nums)
    MT(nums)
    print('Program finish', time.ctime())


if __name__ == '__main__':
    main()