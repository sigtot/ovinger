file = open('poenggrenser_2011.csv')
def csvToDict(file):
	# Converts CSV formatted file into dictionary
	entries = {}

	lines = file.read().splitlines()
	file.close()
	for line in lines:
		try:
			# Prøver int
			entries[line.split(',')[0]] = float(line.split(',')[1])

		except ValueError:
			# Om det ikke er en int, bare legger vil til strengen
			entries[line.split(',')[0]] = line.split(',')[1].replace('"','')

	for i in range(90):
		print(lines[i])

	return entries
linjer = csvToDict(file)

def findAll(linjer):
	return list(linjer.values()).count('Alle')
print('Alle:',findAll(linjer))

def averageLimit(linjer,linjeNavn):
	avgSum = 0
	avgNum = 0
	for name,val in list(linjer.items()):
		if type(val) is float and linjeNavn in name:
			avgSum += val
			avgNum += 1
	return round(avgSum / avgNum,2)
print('Avg:',averageLimit(linjer,'NTNU'))

def minLimit(linjer):
	#items = [list(x) for x in zip(*list(linjer.items()))]
	items = list(linjer.items())
	medPoengsum = []

	for i,e in enumerate([list(x)[1] for x in items]):
		if type(e) is float: medPoengsum.append(items[i])


	#return list(linjer.keys())[list(linjer.values()).index(max(linjer.values()))]
	return min(medPoengsum)
print('Lavest',minLimit(linjer))