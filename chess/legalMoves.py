# OOP?
import superGlobals as sg

def moveIsLegal(move):
	# VECTOR COORDINATES ARE X-Y, IN sg.pieceMatrix THAT WOULD
	# CORRESPOND TO [Y][X], NOT [X][Y]

	# Make sure there's even a piece on the given tile
	piece = sg.pieceMatrix[move[0][1]][move[0][0]]
	if piece == '':
		print('No piece on that tile')
		return False

	# First make sure that we're the right color
	if sg.blackTurn != isLower(piece) and piece != '':
		print('That\'s the wrong color')
		return False

	# And that we're not about to step on our own piece
	target = sg.pieceMatrix[move[1][1]][move[1][0]]
	if sg.blackTurn == isLower(target) and target != '':
		print('You already have a piece on that tile')
		return False

	# Make sure we move at all

	# REDUNDANT, would have stepped on own piece
	v = makeVector(move) # We do need this tho
	if v[0] == 0 and v[1] == 0:
		print('0 length move')
		return False

	# Then we find out if the move fits legal pattern for the given piece
	if not moveFitsPattern(piece,v):
		print('Illegal move')
		return False

	# Also check if our move is obstructed by anything
	if moveIsObstructed(move):
		print('Something is in the way')
		return False

	# Extra pawn stuff
	if not rickHarrison(move,v,piece):
		print('I\'m Rick Harrison and this is my pawn shop')
		return False

	# Otherwise
	return True

def rickHarrison(move,v,piece):
		if piece.lower() != 'p': return True
		def targetEmpty():
			target = sg.pieceMatrix[move[1][1]][move[1][0]]
			return target == ''

		def pieceInSecondRow():
			boardLength = 8 # Make superglobal
			row = move[0][1]
			return row == boardLength - 2 and not sg.blackTurn or row == 1 and sg.blackTurn

		direction = getDirection()

		pawnStraight = [0,1 * direction]
		pawnLong = [0,2 * direction]
		pawnDiag = [[1 * direction, 1 * direction],[-1 * direction, 1 * direction]]

		def debug():
			print('targetEmpty',targetEmpty())
			print('v == pawnStraight',v == pawnStraight)
			print('v == pawnLong',v == pawnLong)
			print('pieceInSecondRow()',pieceInSecondRow())
			print('v in pawnDiag',v in pawnDiag)
			print('v in pawnDiag and not targetEmpty()',v in pawnDiag and not targetEmpty())
			print('rickHarrison',targetEmpty() and (v == pawnStraight or v == pawnLong and pieceInSecondRow()) or v in pawnDiag and not targetEmpty())
		#debug()

		return targetEmpty() and (v == pawnStraight or v == pawnLong and pieceInSecondRow()) or v in pawnDiag and not targetEmpty()

def moveIsObstructed(move):
	# Only handles straight moves
	v = makeVector(move)
	if not (abs(v[0]) == abs(v[1]) or v[0] == 0 or v[1] == 0):
		return False
	for i in range(max(v) - 1):
		if sg.pieceMatrix[move[0][1] + v[1]][move[0][0] + v[0]] != '':
			return True
		v[0] = sub(v[0])
		v[1] = sub(v[1])


def moveFitsPattern(piece,v):
	# Assuming no shit has made it's way into our board

	# Pawn
	if piece.lower() == 'p':
		# Pawn movement direction depends on player color
		# Black side is upper side
		direction = getDirection()
		pawnMoves = [[0, 1 * direction], [0, 2 * direction], [1 * direction, 1 * direction],[-1 * direction, 1 * direction]]
		return v in pawnMoves

	# Knight
	if piece.lower() == 'n':
		#knightMoves = [[-1,2], [1,2], [1,-2], [-1,-2], [-2,1], [2,1], [2,-1], [-2,-1]]
		# Move is valid if for a given vector [a,b]:
			# abs(a) != abs(b)
			# abs(a) in (1,2) and abs(b) in (1,2)

		def happyHorse(v):
			""".  ,    ___________
	           |\/|    |Jolly gee|
	           bd "n.  /----------
	          /   _,"n.___.,--x.
	         <co>'\             Y
	          ~~   \       L   7|
	                H l--'~\  (||
	                H l     H |`'
	                H [     H [
	           ____//,]____//,]___"""
			if abs(v[0]) == abs(v[1]):
				return False
			if abs(v[0]) not in (1,2):
				return False
			if abs(v[1]) not in (1,2):
				return False
			return True

		return happyHorse(v)

	def bish(v):
		# Ya bish
		return abs(v[0]) == abs(v[1])

	def rook(v):
		return not abs(v[0]) or not abs(v[1])

	# Bishop
	if piece.lower() == 'b':
		return bish(v)

	# Rook
	if piece.lower() == 'r':
		return rook(v)

	# Queen
	if piece.lower() == 'q':
		return bish(v) or rook(v)

	# King
	if piece.lower() == 'k':
		return abs(v[0]) <= 1 and abs(v[1]) <= 1

def makeVector(move):
	return [move[1][0] - move[0][0], move[1][1] - move[0][1]]

def isLower(letter):
	return letter == letter.lower()

def sub(n):
	# Subtract one until val reaches zero
	if not n:
		return n
	else:
		return sign(n) * (abs(n) - 1)

def sign(n):
	if n > 0: return 1
	if n < 0: return -1

def getDirection():
	direction = -1
	if sg.blackTurn:
		direction = 1
	return direction