#!/usr/bin/python
# coding=utf-8

import argparse
import math
import sys

v = 'Square 2.1'


def disc(i, j, k):
    d = math.pow(j, 2) - 4 * i * k
    return d


def is_zero(z):
    if z == 0:
        return True
    else:
        return False


def solve(qc, lc, co):
    r = []
    d = disc(qc, lc, co)
    if is_zero(d):
        x = -lc/(2*qc)
        if is_zero(x):
            x = abs(x)
        r.append(x)
    elif d > 0:
        xo = (-lc + math.sqrt(d)) / (2*qc)
        xt = (-lc - math.sqrt(d)) / (2*qc)
        r.extend([xo, xt])
    return d, tuple(r)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Script to solve quadratic equation.\n[a]⋅x² + [b]⋅x + [c] = 0')
    parser.add_argument('a', type=float,
                        help='Quadratic coefficient \'a\'. Non-zero value.')
    parser.add_argument('b', type=float,
                        help='Linear coefficient \'b\'')
    parser.add_argument('c', type=float,
                        help='Coefficient \'c\'')
    parser.add_argument('-v', '--version', action='version',
                        version=v, help='Show program\'s version number and exit.')
    args = parser.parse_args()

    a = args.a
    b = args.b
    c = args.c

    if is_zero(a):
        sys.exit('First argument should not equal \'0\'')

    D, root = solve(a, b, c)
    print 'D = {}'.format(round(D, 2))

    if len(root) == 2:
        print 'x1 = {}; x2 = {}'.format(round(root[0], 2), round(root[1], 2))
    elif len(root) == 1:
        print "x = {}".format(round(root[0], 2))
    else:
        print 'No value'
