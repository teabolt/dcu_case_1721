#!/usr/bin/env python3

class Lamp(object):
    # Model a lamp (light).

    def __init__(self, state=False):
        self.on = state

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        self.on = not self.on

def main():
    l1 = Lamp()
    l2 = Lamp(True)
    l3 = Lamp(False)
    l2.turn_on()
    print(l2.on)
    l2.turn_off()
    print(l2.on)
    l2.toggle()
    print(l2.on)
    print('---')
    for i in range(10):
        l1.toggle()
        print(l1.on)

if __name__ == '__main__':
    main()