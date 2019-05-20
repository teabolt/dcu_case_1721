#!/usr/bin/env python3

import threading

def knocker():
    print('Knock knock')
    print('Race condition')

def opener():
    print('Who there')

def main():
    k = threading.Thread(target=knocker)
    t = threading.Thread(target=opener)
    k.start()
    t.start()
    k.join()
    t.join()

if __name__ == '__main__':
    main()