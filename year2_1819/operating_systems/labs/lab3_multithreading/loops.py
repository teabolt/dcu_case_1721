#!/usr/bin/env python3

from time import sleep, ctime
import inspect
import threading
import random


def loop0():
	print('{} starting at: {}'.format(inspect.stack()[0][3], ctime()))
	sleep(4)
	print('loop0 ending at:', ctime())


def loop1():
	print('loop1 starting at:', ctime())
	sleep(2)
	print('loop1 ending at:', ctime())


def loopn(name, duration=1):
	print('{} started for {} seconds: {}'.format(name, duration, ctime()))
	sleep(duration)
	print('{} ended: {}'.format(name, ctime()))


def main():
	print('Before execution:', ctime())
	# ST()
	# MT()
	MTn(5, [3, 5, 1, 6, 3])

	print('Finished execution:', ctime())


def ST():
	loop0()
	loop1()


def MT():
	th1 = threading.Thread(target=loop0)
	th2 = threading.Thread(target=loop1)
	th1.start()
	th2.start()
	th1.join()
	th2.join()


def MTn(N, durations):
	threads = [threading.Thread(name='Thread boi number {}'.format(i), target=loopn, args=(i,), kwargs={'duration':durations[i]}) for i in range(N)]
	for th in threads:
		th.start()
	print('Meta:', threading.active_count(), threading.enumerate(), threading.current_thread())
	for th in threads:
		th.join()


if __name__ == '__main__':
	main()
