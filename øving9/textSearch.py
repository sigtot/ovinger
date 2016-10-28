# -*- coding: utf8 -*-
#a
def readFromFile(uri):
	file = open(uri)
	return file.read()
readFromFile('helloWorld')

#b
def removeSymbols(st):
	# KAN GJØRES LETTERE MED .replace()
	# Blir færre iterations og

	specialChars = 'æøåÆØÅ '
	newString = ''
	import string as s
	for char in st:
		if char in s.ascii_lowercase + s.ascii_uppercase + specialChars:
			newString += char
		if char == '\n':
			newString += ' '
	return newString.lower()
print(removeSymbols(readFromFile('helloWorld')))

#c
# Count words
def makeDict(uri):
	st = removeSymbols(readFromFile(uri))
	words = {}
	for w in st.split():
		if w not in words:
			# Add w to words
			words[w] = 1
		else:
			words[w] += 1
	return words
print(makeDict('helloWorld'))

#d
#import textSearch as t
#words = t.makeDict('bible')

#Finne vanligste ord
#list(words.keys())[list(words.values()).index(max(words.values()))]