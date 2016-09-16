tall = 4
def gtabell(n):
	for i in range(1,n + 1):
		print('{0}-gangen'.format(i))
		for j in range(1,tall + 1):
			print(j*i)
gtabell(4)