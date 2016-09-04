k = 12
def main():
	n=int(input("Skriv inn et heltall n: "))
	s = 0
	for i in range(n + 1):
		if i % 2: s += i**2
		else: s -= i**2
		if s > k:
			s -= i**2
			print('Resultat med k =',str(k) + ':',s)
			print('Antall ledd:',i - 1)
			return
main()