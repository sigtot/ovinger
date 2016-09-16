# Returnerer True/False i stedet for 1/0
def checkInt(n):
	# Modulo 1 gir null for alle heltall
	if float(n) % 1 == 0: return True
	else: return False

def checkEven(n):
	# Modulo 2 gir null for alle partall
	if float(n) % 2 == 0: return True
	else: return False

def checkSign(n):
	if float(n) > 0: return True
	elif float(n) < 0: return False
	else: return 2

def compareNums(n,p):
	if n > p or n < p: return False
	else: return True

def main():
	n = input('Oppgi tall: ')
	if(checkInt(n)):
		print('Dette er et heltall')
		if checkEven(n): print('Dette er et partall')
		else: print('Dette er et oddetall')
	else: print('Dette er ikke et heltall')
	if checkSign(n) == True: print('Dette er et positivt tall')
	elif checkSign(n) == 2: print('Dette tallet er hverken positivt eller negativt')
	else: print('Dette er et negativt tall')
	main() #Starter fra begynnelsen
main()