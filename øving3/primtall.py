def primtall(n):
	for i in range(2,n):
		for j in range(2,i):
			if i%j is 0: break
		else: print(i)
primtall(100)