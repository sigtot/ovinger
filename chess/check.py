import superGlobals as sg
import legalMoves as lm
import moves

def check(justChecking = False,king = None,k = None):
	# Assuming 2 kings
	def checkStraight(center,kingPiece,justChecking = False):
		for x in (True,False):
			for direction in (-1,1):
				for tileDelta in range(1,sg.boardLength):
					try:
						if x: tileToCheck = [center[0], center[1] + tileDelta * direction]
						else: tileToCheck = [center[0] + tileDelta * direction, center[1]]
						piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
						if min(tileToCheck) < 0: break;
						if piece != '':
							if not sameCase(kingPiece,piece) and piece.lower() in ('r','q'):
								if not justChecking: print('Check!')
								if not justChecking: checkMate()
								return True
							break
					except IndexError:
						break
		return False

	def checkDiag(center,kingPiece,justChecking = False):
		for x in (-1,2):
			for y in (-1,2):
				for tileDelta in range(1,int(sg.boardLength / 2)):
					try:
						tileToCheck = [center[0] + tileDelta * y, center[1] + tileDelta * x]
						piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
						if min(tileToCheck) < 0: break;
						if piece != '':
							if not sameCase(kingPiece,piece) and piece.lower() in ('b','q'):
								#print('Check! (Diagonal)')
								if not justChecking: checkMate()
								return True
							break
					except IndexError:
						break

	def checkClose(center,kingPiece,justChecking = False):
		alreadyChecked = [list(center)]
		for i in range(-1,2):
			for j in range(-1,2):
				tileToCheck = [sg.ia(center[0], i, 0, sg.boardLength - 1),sg.ia(center[1], j, 0, sg.boardLength - 1)]
				if tileToCheck in alreadyChecked: continue
				alreadyChecked.append(tileToCheck)
				piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
				if piece.lower() == 'k':
					#print('Check! (Close)')
					if not justChecking: checkMate()
					return True

	def checkPawn(center,kingPiece,justChecking = False):
		def checkItOut(direction):
			for x in (-1,1):
				try:
					tileToCheck = [center[0] + x,center[1] + 1]
					piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
					if not sameCase(piece,kingPiece) and piece.lower() == 'p':
						#print('Check! (Pawn)')
						if not justChecking: checkMate()
						return True
				except IndexError:
					continue

		if sg.isLower(kingPiece):
			#Black can be checked from the front
			checkItOut(1)
		else:
			checkItOut(-1)

	def grumpyHorse(center,kingPiece,justChecking = False):
		""" ____________________
			< Quit your meddlin' >
			 --------------------
			    \       
			     \      
			      \      _\^
			       \   _- oo\
			           \---- \______
			                 \       )\
			                ||-----||  \
			                ||     ||"""
		def jumpAround(jump):
			for x in (-1,1):
				for y in (-1,1):
					try:
						tileToCheck = [center[0] + jump[0] * x, center[1] + jump[1] * y]
						if min(tileToCheck) < 0: continue
						piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
						if not sameCase(piece,kingPiece) and piece.lower() == 'n':
							#print('Check! (Knight)')
							if not justChecking: checkMate()
							return True
					except IndexError:
						continue
		jumpAround([1,2])
		jumpAround([2,1])

	def checkMate():
		if sg.blackTurn: 
			center = getIndexes('k')
			k = 'k'
		else: 
			center = getIndexes('K')
			k = 'K'

		alreadyChecked = [list(center)]
		for i in range(-1,2):
			for j in range(-1,2):
				tileToCheck = [sg.ia(center[0], i, 0, sg.boardLength - 1),sg.ia(center[1], j, 0, sg.boardLength - 1)]
				if tileToCheck in alreadyChecked: continue
				alreadyChecked.append(tileToCheck)
				piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
				if piece.lower() == '':
					if not performCheck(tileToCheck,k,True):
						return False
		# Kind of in check mate
		if not justChecking: m8()
					
		#I'm too tired for this shit
		# 1. Check if the king can move to each tile
		# 2. Move the king to every possible tile
		# 3. If every position returns a True check(), current user is in check

		return False


	def performCheck(king,k,justChecking = False):
		if (checkStraight(king,k,justChecking) or
			checkDiag(king,k,justChecking) or
			checkClose(king,k,justChecking) or
			checkPawn(king,k,justChecking) or
			grumpyHorse(king,k,justChecking)):
			return True

	if justChecking:
		return performCheck(king,k,True)
	else:
		for k in ('k','K'):
			king = getIndexes(k)
			return performCheck(king,k)

def m8():
	# Move every piece to ever tile on the board and back again
	# For every move, 
		# Check if checkMate() and moveIsLegal()
			# Return True
		#Return False
	if sg.blackTurn: 
		king = getIndexes('k')
		k = 'k'
	else: 
		king = getIndexes('K')
		k = 'K'
	for a,row in enumerate(sg.pieceMatrix):
		for b,tile in enumerate(row):
			if tile != '':
				# Verify correct color
				if sg.blackTurn and not sg.isLower(tile): continue
				if not sg.blackTurn and sg.isLower(tile): continue

				# Create moves for each tile
				for c in range(sg.boardLength):
					for d in range(sg.boardLength):
						move = [[b,a],[d,c]] # XY flip
						if lm.moveIsLegal(move,True):
							# Perform move
							# Save old piece for later
							oldPiece = tile
							moves.performMove(move,True)
							king = getIndexes(k)
							if not check(True,king,k):
								# Move back
								moves.performMove(move[::-1],True)
								sg.pieceMatrix[a][b] = oldPiece
								return True
							# Move back
							moves.performMove(move[::-1],True)
							sg.pieceMatrix[a][b] = oldPiece

	print('Check mate')



def sameCase(l1,l2):
	return sg.isLower(l1) == sg.isLower(l2)

def sameLetter(l1,l2):
	return l1.lower() == l2.lower()

def getIndexes(l):
	for i,row in enumerate(sg.pieceMatrix):
		if l in row:
			return i,row.index(l)

def setCheck(check):
	if sg.blackTurn: sg.check[0] = check
	else: sg.check[1] = check