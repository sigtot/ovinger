# -*- coding: utf8 -*-
import math

print('------ a ------')
def makeBoard(bs):
	side = math.sqrt(len(bs))
	if int(side) != side:
		print('Non square board')
		return
	side = int(side)
	board = []
	for i in range(side):
		row = []
		for j in range(side):
			e = j+side*i
			if bs[e] == '.': 	row.append(None)
			else:				row.append(bs[e])
		board.append(row)
	return board

boardString = 'rkn.r.p.....P..PP.PPB.K..'
board = makeBoard(boardString)
print(board)

def showBoard(board):
	pieces = [['k','q','r','b','n','p','K','Q','R','B','N','P'],['♚','♛','♜','♝','♞','♟','♔','♕','♖','♗','♘','♙']]
	for i,l in enumerate(board):
		line = ''
		for j,p in enumerate(l):
			if not p: 
				# Either black or white square
				if (i + j) % 2 != 0:
					# Even squares are odd
					line += '◻'
				else: line += '◼'
			else:
				line += pieces[1][pieces[0].index(p)]
		#print(line)
		print(line.replace("", " ")[1: -1]) #For mellomrom mellom feltene

showBoard(board)

print('\n------ b ------')

def getPiece(board, x, y):
	return board[5 - y][x - 1]

print(getPiece(board,2,1))
print(getPiece(board,5,2))

print('\n------ c ------')
def case(st):
	# False i lower, True is upper
	return st.lower() != st

def getLegalMoves(board, x, y):
	piece = getPiece(board, x, y)
	moves = []
	if piece == 'P':
		# Ett skritt fram
		# Tom rute rett foran
		if not getPiece(board, x, y + 1):
			moves.append([x,y + 1])

		# To skritt fram
		# Tom rute to ruter foran
		if not getPiece(board, x, y + 2):
			moves.append([x,y + 2])

		try:
			# Motbrikke til venstre
			if getPiece(board, x - 1, y + 1) and case(piece) != case(getPiece(board, x - 1, y + 1)):
				moves.append([x - 1, y + 1])

			# Motbrikke til høyre
			if getPiece(board, x + 1, y + 1) and case(piece) != case(getPiece(board, x + 1, y + 1)):
				moves.append([x + 1, y + 1])
		except IndexError:
			pass
			

	if piece == 'p':

		# Ett skritt fram
		# Tom rute rett foran
		if not getPiece(board, x, y - 1):
			moves.append([x,y - 1])

		# To skritt fram
		# Tom rute to ruter foran
		if not getPiece(board, x, y - 2):
			moves.append([x,y - 2])

		try:
			# Motbrikke til venstre
			if getPiece(board, x - 1, y - 1) and case(piece) != case(getPiece(board, x - 1, y - 1)):
				moves.append([x - 1, y - 1])

			# Motbrikke til høyre
			if getPiece(board, x + 1, y - 1) and case(piece) != case(getPiece(board, x + 1, y - 1)):
				moves.append([x + 1, y - 1])



		except IndexError:
			pass


	return moves

print(getLegalMoves(board, 4, 2))
print(getLegalMoves(board, 2, 4))
#print(getLegalMoves(board, 3, 3))