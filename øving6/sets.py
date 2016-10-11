def allUnique(lst): return len(lst) == len(set(lst))

def removeDuplicates(lst): return list(set(lst))

def relativeComplement(a,b): return list(set(a) - set(b))

#Ekstra
import numpy as np
def showArray():
	arr = np.arange(1,16)
	arr = arr.reshape(3,5)
	arr = np.transpose(arr)
	return arr

ver = np.array([2,0])
hor = np.array([0,2])

def areOrthogonal(a,b):
	# Prikkprodukt er null hvis vektorene er vinkelrette
	if np.dot(a,b) == 0: return True
	else: return False