import superGlobals as sg
import legalMoves as l
boardLength = 8 #meh
letters = ['a','b','c','d','e','f','g','h']

def convertMove(move):
	move = str(move)
	vector = []
	if len(move) != 4: return False
	try:
		if move[0] not in letters or move[2] not in letters: return False
		if int(move[1]) not in range(1,9) or int(move[3]) not in range(1,9): return False
		
		for i in range(0,4,2):
			# Boardlength because the board is backwards or some shit
			vector.append([letters.index(move[i]), boardLength - int(move[i+1])])
		return vector
	except ValueError:
		# Second and fourth letter might not be int
		return False

def getMove():
	if sg.blackTurn: player = 'Black'
	else: player = 'White'
	move = convertMove(input('{}, your turn: '.format(player)))
	if not move:
		# convertMove() returned False
		print('Input moves like this: c4e6')
		return getMove()
	if l.moveIsLegal(move): return move
	else: return getMove()

def performMove(move,temporary = False):
	# Remember [X,Y] in move corresponds to [Y][X] in matrix
	# target = piece
	sg.pieceMatrix[move[1][1]][move[1][0]] = sg.pieceMatrix[move[0][1]][move[0][0]]
	old = sg.pieceMatrix[move[1][1]][move[1][0]]
	#piece = ''
	sg.pieceMatrix[move[0][1]][move[0][0]] = ''
	if not temporary: sg.blackTurn = not sg.blackTurn
	return old