mark = ('x','o')
import os

#a
def printBoard(board):
	print('    1   2   3')
	print('  -------------')
	print('1 | {} | {} | {} |'.format(board[0][0], board[0][1], board[0][2]))
	print('  -------------')
	print('2 | {} | {} | {} |'.format(board[1][0], board[1][1], board[1][2]))
	print('  -------------')
	print('3 | {} | {} | {} |'.format(board[2][0], board[2][1], board[2][2]))
	print('  -------------')

#b
def gameWon(board):
	def checkStraight(board):
		for row in board:
			if row.count('x') == 3: win(1)
			if row.count('o') == 3: win(2)
	
	def checkDiagonal(board):
		diagonal = [board[x][x] for x in range(3)]
		if diagonal.count('x') == 3: win(1)
		if diagonal.count('o') == 3: win(2)

	checkStraight(board)
	checkStraight(board = [list(x) for x in zip(*board)])

	checkDiagonal(board)
	checkDiagonal([list(x) for x in board.__reversed__()])

def win(playerNum):
	print('Player {} wins'.format(playerNum))
	exit()

#c
def getNames():
	print('Please enter player names:')
	name1 = input('Player 1: ')
	name2 = input('Player 2: ')
	clearScreen()
	print('Welcome {} and {}. glhf'.format(name1,name2))
	return name1,name2

#d
def moveLegal(board,x,y):
	return board[x][y].isspace()

#e
def fixInput(st):
	try:
		x, y = int(st.split()[1]), int(st.split()[0])
	except IndexError:
		return fixInput(input('Remember space between values: '))

	except ValueError:
		return fixInput(input('Please only input numbers: '))
	try:
		if not( x >= 1 and x <= 3 and y >= 1 and y <= 3):
			return fixInput(input('Only numbers from 1-3 are accepted: '))
	except TypeError:
		#Redundant after ValueError?
		return fixInput(input('Oops, looks like you didn\'t input real coordinates: '))
	return x,y

def move(turn,board,players):
	print('Your turn,',players[turn])
	while True:
		x,y = fixInput(input('Input coordinates (1-3, separated by space): '))
		x,y = x - 1, y - 1
		if moveLegal(board,x,y):
			board[x][y] = mark[turn]
			break
		else:
			print('Illegal move')
	return int(not turn)

def clearScreen():
	absolutely_unused_variable = os.system("clear")

def main():
	clearScreen()
	board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	players = getNames()
	turn = 0

	while True:
		printBoard(board)
		gameWon(board)
		turn = move(turn,board,players)
		clearScreen()
main()
