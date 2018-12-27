import sys
import math

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

    i = 0
    r = start_r
    while r < end_r:
        r = start_r + i*inc_r
        print('{:>{}.1f} {:>15.2f} {:>15.2f}'.format(r, len(h4), 4*math.pi*r**2, 4/3*math.pi*r**3))
        i += 1

if __name__ == '__main__':
    main()
