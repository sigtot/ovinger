def fibonacci(k):
	s = 0
	for i in range(k + 1):
		if i == 0: f = 0
		elif i == 1: 
			last = f
			f = 1
		else: 
			blast = last
			last = f
			f = last + blast
		s += f
	return f,s

def fList(k):
	# Ikke den mest optimale metoden. 
	# fibonacci() funksjonen kjøres en gang for hvert fall i rekka
	for i in range(k): 
		print(fibonacci(i))

fList(2000)