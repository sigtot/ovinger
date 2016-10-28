# -*- coding: utf8 -*-
birthdays = {
'22 nov': ['Lars', 'Mathias'],
'10 des': ' Elle ',
'30 okt': ['Veronica', 'Rune'],
'12 jan': 'Silje',
'31 okt': 'Willy',
'8 jul': ['Brage', 'Øystein'],
'1 mar': 'Nina'
}

def addBirthDayToDate(date, name):
	try:
		birthdays[date].append(name)

	except AttributeError:
		#a
		# Kun ett navn (string) for denne bursdagen
		birthdays[date] = [name, birthdays[date]]

	except KeyError:
		#b
		# Dato finnes ikke
		birthdays[date] = name

#a
print('------ a ------')
print('Birthdays før:', birthdays)
addBirthDayToDate('12 jan', 'Sindre')
print('Birthdays etter:', birthdays)

#b
print('\n------ b ------')
print('Birthdays før:', birthdays)
addBirthDayToDate('9 feb', 'Lillian')
print('Birthdays etter:', birthdays)