import sys
import math

# ax^2 + bx + c = 0

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

D = math.pow(b,2) - 4 * a * c
print D
if D > 0:
	x_one = (-b + math.sqrt(D)) / (2*a)
	x_two = (-b - math.sqrt(D)) / (2*a)
	print x_one, x_two
elif D == 0:
	x = -b/(2*a)
	print x
else:
	print 'No value'
