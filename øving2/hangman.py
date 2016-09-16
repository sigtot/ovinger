import getpass
word = getpass.getpass('Skriv inn et løsningsord (bokstavene er skjulte): ')
savedWord = word
word = list(word)
liv = int(input('Skriv inn antall liv: '))
letterList = [True] * len(word)

def displayWord():
	s = ''
	iterator = 0
	for i in letterList:
		if i: s += '#'
		else: s += savedWord[iterator]
		iterator += 1
	print('Ordet er:',s)
displayWord()
while True in letterList:
	# False når alle indexene er false (alle bokstavene er gjettet)
	while True:
		l = input('Skriv inn en bokstav: ')
		if(len(l) == 1): break # Godtas om det kun er 1 bokstav
		print('Du kan kun skrive inn en bokstav')
	if(l not in word): liv -= 1
	if(liv < 1):
		print('Du døde, spillet er over')
		print('Ordet var',savedWord)
		break
	while l in word:
		letterList[word.index(l)] = False
		word[word.index(l)] = '0'
	print('Du har',liv,'liv igjen')
	displayWord()
if(True not in letterList):
	print('Gratulerer, du vant')
	print('Ordet var',savedWord)