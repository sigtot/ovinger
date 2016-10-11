def countCoins(lst):
	s = 0
	for i in lst:
		s += i
	return s

coins = [20,10,5,1]
def listCoins(x):
	change = []
	while x > 0:
		for c in coins:
			for i in range(1, (x // c) + 1):
				change.append(c)
				x = x - c
	return change

def numCoins(x):
	nums = [0,0,0,0]
	while x > 0:
		for n in range(len(nums)):
			for i in range(1, (x // coins[n]) + 1):
				nums[n] += 1
				x = x - coins[n]
	return nums

def numCoinsList(lst):
	coinList = []
	for i in lst:
		coinList.append(numCoins(i))
	return coinList

#print('Test:',numCoinsList([12,23,34,45,56,67,78,89,90,98,87,65,54,43,21]))

def checkWeight(lst):
	weights = [9.9, 6.8, 7.85, 4.35]
	totalWeight = 0
	i = 0
	for c in lst:
		totalWeight += c * weights[i]
		i += 1
	return totalWeight

	# Har roundoff bug