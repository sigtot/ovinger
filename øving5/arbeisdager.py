# -*- coding: utf8 -*-
weekdays = ('man','tir','ons','tor','fre','lør','søn')
weekend = (5,6)
dayIndex = 0
startYear = 1900
def isLeapYear(y):
	if y % 400 == 0:
		return True
	elif y % 100 == 0:
		return False
	elif y % 4 == 0:
		return True
	return False

def firstDayList(y):
	d = 0
	i = 0
	while i < y - startYear:
		# Trekker fra heltallsdivisjonen ganget med antall dager i en uke
		# Dette gir oss et tall mellom 0 og 6
		print(i + startYear,weekdays[d - (d // len(weekdays)) * len(weekdays)])

		i += 1
		d += 1
		if isLeapYear(i + startYear - 1): d += 1

def firstDay(y):
	# What is code reuse?
	d = 0
	i = 0
	while i < y - startYear:
		# Trekker fra heltallsdivisjonen ganget med antall dager i en uke
		# Dette gir oss et tall mellom 0 og 6

		i += 1
		d += 1
		if isLeapYear(i + startYear - 1): d += 1
	return d - (d // len(weekdays)) * len(weekdays)

firstDay(1919)
def workDay(d):
	if d in weekend: return False
	else: return True

def numWorkDays(y):
	initialDay = firstDay(y)
	n = 0
	# Brute force that shit
	yearLength = 365
	if isLeapYear(y): yearLength += 1
	date = 0
	while date < yearLength:
		day = date + initialDay - ((date + initialDay) // len(weekdays)) * len(weekdays)
		date += 1
		if not workDay(day): continue
		n += 1
	return n

def listWorkDays(y):
	for i in range(startYear,y):
		print(i,'har',numWorkDays(i),'arbeidsdager.')

print('-------- Første dager --------')
firstDayList(1920)
print('\n------- Arbeidsdager -------')
listWorkDays(1920)