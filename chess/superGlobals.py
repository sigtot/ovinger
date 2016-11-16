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
	['r','','b','q','k','b','n','r'],
	['p','p','p','p','p','p','p','p'],
	['','','','','','','',''],
	['','','','','','n','',''],
	['','','','K','','','',''],
	['','','','','','','',''],
	['P','P','P','P','P','P','P','P'],
	['R','N','B','Q','','B','N','R']
]
blackTurn = False
boardLength = 8

def lop():
	for y in pieceMatrix:
		for x in y:
			print(x)

def isLower(letter):
	return letter == letter.lower()

def ia(number, adder, min = 0, max = 1000):
	# Interval arithmetic function
	old = number
	number += adder
	if number not in range(min,max + 1): return old
	else: return number