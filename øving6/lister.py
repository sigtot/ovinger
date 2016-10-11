#a
numberList = list(range(100)) #Liste fra 0 til 99
print('------ Liste fra 0 til 99 ------')
print(numberList)

#b
#Printer summen av tall delelige med 10 og 3
sum = 0
for i in numberList:
	if i % 3 == 0 or i % 10 == 0: sum += i
print('\n------ Sum av tall delelige med 10 og 3 ------')
print(sum)

#c
#Bytt plass på odde og partall
for i in numberList:
	if i % 2 != 0:
		# Oddetall funnet

		# OBS
		# Spesialtilfelle for lister fra 0 til x
		# Indexen er lik listeelementet (arr[i] == i)
		# Bytter plass
		previous = numberList[i - 1] 
		numberList[i - 1] = i
		numberList[i] = previous
print('\n------ Bytter om på odde og partall ------')
print(numberList)

#d
#Reverserer
newList = []
for i in range(len(numberList) - 1,-1,-1):
	newList.append(numberList[i])
print('\n------ Reverserer ------')
print(newList)