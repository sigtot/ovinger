def isSorted(lst):
	for i,e in enumerate(lst):
		try: 
			if e > lst[i + 1]: return False
		except:
			pass
	return True

#a
def bubbleSort(lst):
	lst = lst[:]
	while not isSorted(lst):
		try:
			for i,e in enumerate(lst):
				if e > lst[i + 1]:
					lst[i],lst[i + 1] = lst[i + 1],lst[i]
		except:
			lel = 'gee'
	return lst

#b
def selectionSort(lst):
	lst = lst[:]
	newList = []
	while len(lst):
		biggest = 0
		i = 0
		for e in lst:
			if e < lst[biggest]:
				biggest = i
			i += 1
		newList.append(lst.pop(biggest))
		# Legger bakers istedenfor fremst
		# Skal vi sortere baklengs?
	return newList

#c

def compareSorts(n):
	import time
	import random

	#Genererer en lang liste med n tilfeldige tall opp til n størrelse
	lst = random.sample(range(n),n)

	now = int(round(time.time() * 1000))
	bubbleSort(lst)
	bubbleDelta = int(round(time.time() * 1000)) - now

	# Reset now
	now = int(round(time.time() * 1000))
	selectionSort(lst)
	selectionDelta = int(round(time.time() * 1000)) - now

	#Print
	print("Bubble sort took",str(bubbleDelta)+"ms")
	print("Selection sort took",str(selectionDelta)+"ms")

#Noen tester
"""
>>> s.compareSorts(100)
Bubble sort took 6ms
Selection sort took 1ms

>>> s.compareSorts(1000)
Bubble sort took 188ms
Selection sort took 45ms

>>> s.compareSorts(2000)
Bubble sort took 708ms
Selection sort took 182ms

>>> s.compareSorts(3000)
Bubble sort took 1610ms
Selection sort took 409ms

Konklusjon: Bubblesort bruker lengst tid
"""