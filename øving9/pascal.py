import math

def nCr(n,r):
	f = math.factorial
	return int(f(n) / f(r)  / f(n-r))

def makePascal(n):
	triangle = []
	for i in range(n):
		row = []
		for j in range(i + 1):
			row.append(int(nCr(i,j)))
		triangle.append(row)
	return triangle

def printPascal(triangle):
	for row in triangle:
		print(''.join([str(x) for x in row]))
printPascal(makePascal(10))

def polynomial(n):
	poly = '(x+y)^' + str(n) + " = "
	for i,j in zip(range(n + 1),reversed(range(n + 1))):
		if nCr(n,i) != 1: poly += str(nCr(n,i))
		
		if j == 1: 	poly += 'y'
		else: 		poly += 'y^' + str(j)

		if i == 1: 	poly += 'x'
		else: 		poly += 'x^' + str(i)

		if j > 0: poly += ' + '

	# Ommit ones
	poly = poly.replace('y^0','')
	poly = poly.replace('x^0','')
	return poly

print(polynomial(6))