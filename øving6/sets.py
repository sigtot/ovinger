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