"""pieceMatrix = [
	['r','n','b','q','k','b','n','r'],
	['p','p','p','p','p','p','p','p'],
	['','','','','','','',''],
	['','','','','','','',''],
	['','','','','','','',''],
	['','','','','','','',''],
	['P','P','P','P','P','P','P','P'],
	['R','N','B','Q','K','B','N','R']
]"""

pieceMatrix = [
	['r','n','b','q','','b','n','r'],
	['p','p','p','p','p','p','p','p'],
	['','','','','','','',''],
	['','','','','','','',''],
	['','','','k','','Q','',''],
	['','','','','','','R','R'],
	['P','P','P','P','P','P','P','P'],
	['','N','B','','K','B','N','']
]

"""pieceMatrix = [
	['r','','b','q','k','b','n','r'],
	['p','p','p','p','p','p','p','p'],
	['','','','','','','',''],
	['','','','','','n','',''],
	['','','','','','','',''],
	['','','','q','','','',''],
	['P','P','P','P','','P','P','P'],
	['R','N','B','Q','K','B','N','R']
]"""
blackTurn = False
boardLength = 8
check = [False,False]

def lop():
	for y in pieceMatrix:
		for x in y:
			print(x)

def isLower(letter):
	return letter == letter.lower()

def ia(number, adder, min = 0, max = 1000):
	# Interval arithmetic function
	# Performs arithmetic operations within an interval
	old = number
	number += adder
	if number not in range(min,max + 1): return old
	else: return number

def getCheck():
	if blackTurn: return check[0]
	else: return check[1]