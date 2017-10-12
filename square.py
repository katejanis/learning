#v1.2

import sys
import math

# ax^2 + bx + c = 0

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

def discriminant(x, y , z):
    d = math.pow(y,2) - 4 * x * z
    return d

D = discriminant(a, b, c)


if a == 0:
    print 'First argument should not be equal zero'
else:
    print "D = %s" % D
    if D > 0:
        x_one = (-b + math.sqrt(D)) / (2*a)
        x_two = (-b - math.sqrt(D)) / (2*a)
        print "x1 = %s, x2 = %s" % (x_one, x_two)
    elif D == 0:
        x = -b/(2*a)
        print "x = %s" % x
    else:
        print 'No value'
