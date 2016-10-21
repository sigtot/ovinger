"""def stringEqual(st1,st2):
	return str(st1) == str(st2)"""
#a
def stringEqual(st1,st2):
	longest = max(len(str(st1)),len(str(st2)))
	try:
		for i in range(longest):
			if str(st1)[i] != str(st2)[i]: return False
		return True
	except:
		return False

#b
def stringReverse(st):
	newSt = ''
	for e in reversed(str(st)):
		newSt += e
	return newSt

#c
def palindrome(st):
	return str(st) == stringReverse(str(st))

#d
def stringContains(child,parent):
	child = str(child)
	parent = str(parent)

	try:
		for i,e in enumerate(parent):
			def stuff():
				if e == child[0]:
					# First letter is good
					for j,f in enumerate(child):
						if f != parent[i + j]: 
							#Continue the outer loop
							return -2
					# for loop finished
					return i
				return -2
			# no finds
			if stuff() != -2:
				return stuff()
	except:
		return -1
	return -1