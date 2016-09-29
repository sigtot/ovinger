# -*- coding: utf8 -*-
import os
maxAge = 25
minAge = 16

numFemale = 0
numMale = 0
numFag = 0
numItgk = 0
totalHours = 0

def end():
	#Det er ikke mulig å hente svarene igjen, de slettes når python session lukkes.
	print('\nTakk\n')
	print('------ Denne undersøkelsen ------')
	print('Antall kvinner:',int(numFemale))
	print('Antall menn:',int(numMale))
	print('Antall som tar fag:',int(numFag))
	print('Antall som går ITGK',int(numItgk))
	print('Totale antall timer',int(totalHours))
	if numFag: print('Avg timer:',int(totalHours/numFag)) # Avoid division by zero
	os._exit(1) #exit without throwing exception

def ask(q):
	a = input(q)
	if a in ('hade','Hade'): end()
	else: return a

print('Skriv inn kjønn og alder')
def getBasics():
	# Age
	def getAge():
		try:
			a = float(ask('Alder: '))
			return a
		except: return getAge()

	# Sex
	def getSex():
		s = ask('Kjønn [f/m]: ')
		if s == 'f': 
			global numFemale
			numFemale += 1
			return True
		elif s == 'm': 
			global numMale
			numMale += 1
			return False
		else: return getSex()

	return getAge(), getSex()

# Check if age is within threshold
def checkAge(a):
	if a not in range(minAge, maxAge + 1):
		print('Ikke i aldersgruppen')
		age,female = getBasics()
		checkAge(age)

def tarFag():
	f = ask('Tar du et fag? [Ja,Nei]')
	if f in ('Ja','ja'): return True
	elif f in ('Nei','nei'): return False
	else: return tarFag()

def tarItgk(a):
	if(a < 22): ans = input('Tar du ITGK? [Ja,Nei]')
	else: ans = input('Tar du virkelig ITGK? [Ja,Nei]')

	if ans in ('Ja','ja'): 
		return True
		global numItgk
		numItgk += 1
	elif ans in ('Nei','nei'): return False
	else: return tarItgk(age)
	return ans

def getHours():
	try:
		h = float(ask('Hvor mange timer bruker du i uka? '))
		return h
	except: return getHours()

def main():
	global numFemale 
	global numMale
	global numFag
	global numItgk
	global totalHours

	age,female = getBasics()
	checkAge(age)
	fag = tarFag()
	if fag:
		global itgk
		itgk = tarItgk(age)
		hours = getHours()
		numFag += 1
		totalHours += hours
	print('\nTakk\n')
	main()
main()