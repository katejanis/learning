#!/usr/bin/python

import argparse
import math
import sys

v = 'Square 2.0'
parser = argparse.ArgumentParser(description='Script to solve quadratic equation.\nax2 + bx + c = 0')
parser.add_argument("a", type=float,
                    help="Quadratic coefficient 'a'. Non-zero value.")
parser.add_argument("b", type=float,
                    help="Linear coefficient 'b'")
parser.add_argument("c", type=float,
                    help="Coefficient 'c'")
parser.add_argument('-v', '--version', action='version',
                    version=v, help="Show program's version number and exit.")
args = parser.parse_args()


def discriminant(i, j, k):
    disc = math.pow(j, 2) - 4 * i * k
    return disc


def is_zero(z):
    if z == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    a = args.a
    b = args.b
    c = args.c

    if is_zero(a):
        sys.exit("First argument should not equal '0'")

    D = discriminant(a, b, c)

    print "D = %s" % D

    if D > 0:
        x_one = (-b + math.sqrt(D)) / (2*a)
        x_two = (-b - math.sqrt(D)) / (2*a)
        print "x1 = %s, x2 = %s" % (round(x_one, 2), round(x_two, 2))
    elif D == 0:
        x = -b/(2*a)
        if x == 0:
            x = abs(x)
        print "x = %s" % round(x, 2)
    else:
        print 'No value'
