import string
poeng = int(input('Skriv inn din poengsum'))
karakterer = [89,77,65,53,41,0]
def findK():
	j = 0
	for i in karakterer:
		if(poeng >= i): 
			print('Du fikk karakter:',string.ascii_uppercase[j])
			return
		j += 1
findK()