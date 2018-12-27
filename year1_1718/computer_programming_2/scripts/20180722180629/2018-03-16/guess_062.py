from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

# Find z *efficiently* by calling guess() (and without peeking at z!)
def find():
    high = top
    low = bottom
    while low < high:
        mid = (low+high)//2
        g = mid
        if guess(g) == -1: # g < z, g is less than z
            # increase g
            # increase low
            low = mid+1
        else: # guess(g) == 1: g > z, g is bigger than z
            # reduce g
            # decrease high
            high = mid
        g = low

    return g

def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
