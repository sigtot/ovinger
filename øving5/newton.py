import math
def f(x):
	return (x-12)*math.e**(5*x)-8*(x+2)**2

def g(x):
	return -x-2*x**2-5*x**3+6*x**4

print(f(12))
print(g(5))