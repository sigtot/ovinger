import math
h_initial = 0.001
x_initial = 0
tol_initial = 0.001

def f(x):
	return (x-12)*math.e**(5*x)-8*(x+2)**2

def g(x):
	return -x-2*x**2-5*x**3+6*x**4

def diff(u, x, h=h_initial):
	return (u(x+h/2) - u(x-h/2))/h

def newton(u, x=x_initial, tol=tol_initial, h=h_initial):
	i = 0
	while abs(u(x)) > tol and i < 10000:
		i += 1 # Capped at 10000 iterations
		x = x - u(x)/diff(u,x,h)
	return round(x,4)

print('g(x) = 0 for x =',newton(g,7))
print('g(x) = 0 for x =',newton(g,0.3))
print('f(x) = 0 for x =',newton(f))
print('f(x) = 0 for x =',newton(f,15))