#!/usr/bin/python3.5
import sys
def gcd(a,b):
	while b:
		bold = b
		b = a % b
		a = bold
	return a

def reduceFraction(a,b):
	while True:
		divisor = gcd(a,b)
		if divisor == 1: break
		a /= divisor
		b /= divisor
	return int(a),int(b)

a,b = reduceFraction(int(sys.argv[1]),int(sys.argv[2]))
a = str(a)
b = str(b)
print(a+'/'+b)
