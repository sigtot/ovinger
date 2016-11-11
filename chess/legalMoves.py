import superGlobals as sg

#def moveIsLegal(move):
	# First make sure that we're the right color

def moveFitsPattern(piece,move):
	# Assuming no shit has made it's way into our board

	# Pawn
	if piece.lower() == 'p':
		# Pawn movement direction depends on player color
		# Black side is upper side
		direction = -1
		if sg.blackTurn:
			direction = 1
		pawnMoves = [[0, 1 * direction], [0, 2 * direction], [1 * direction, 1 * direction],[-1 * direction, 1 * direction]]
		if makeVector(move) in pawnMoves:
			return True

def makeVector(move):
	return [move[1][0] - move[0][0], move[1][1] - move[0][1]]