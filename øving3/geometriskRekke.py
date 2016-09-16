tol = 0.001
def series(r, n=None):
	sum = 0
	lim = 1/(1 - r)
	try:
		# Returner sum med r og n
		for i in range(n + 1):
			sum += r**i
	except:
		# Returner konvergerende sum
		i = 0
		while True:
			sum += r**i
			i += 1
			if(sum > lim - tol): break;
		print('For å være innenfor totalgrensen {0} kjørte løkken {1} ganger'.format(tol, i + 1))
		print('Differansen mellom virkelig og estimert verdi var da',lim - sum)
	return sum


print('Sum av rekken er',series(0.5))
print('\nSum av rekken med 4 ledd er',series(0.5,4))