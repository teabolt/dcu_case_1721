from multiprocessing import *
import random

def sayHi(message, i=None, total=None):
    print("{} for the {} time out of {}, from process {}".format(message, i, total, current_process().pid))

def procEx():
    print("Hi from process", current_process().pid, "(parent process)")

    N = 3
    otherProcs = [Process(target=sayHi, args=(chr(random.randint(0, 100)),), kwargs=({'total':N, 'i':i})) for i in range(N)]
    for otherProc in otherProcs:
    	otherProc.start()


def sayMyName(lock, name):
    lock = Lock()
    lock.acquire()
    print('Greetings {}! This is your servant {}, number {}'.format(name, current_process().name, current_process().pid))
    lock.release()

def stdout():
    print('T3st' + current_process().name)


def main():
    lock = Lock()
    name = input('Enter your name: ')
    N = int(input('Enter how many processes do you want: '))
    for i in range(N):
        Process(target=sayMyName, args=(lock, name,), name=str(i)).start()
        # Process(target=stdout, ).start()

if __name__ == '__main__':
	main()