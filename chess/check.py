import superGlobals as sg

def check():
	# Assuming 2 kings
	def getIndexes(l):
		for i,row in enumerate(sg.pieceMatrix):
			if l in row:
				return i,row.index(l)

	def checkStraight(center,kingPiece):
		for x in (True,False):
			for direction in (-1,1):
				for tileDelta in range(1,sg.boardLength):
					try:
						if x: tileToCheck = [center[0], center[1] + tileDelta * direction]
						else: tileToCheck = [center[0] + tileDelta * direction, center[1]]
						piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
						print(piece)
						if min(tileToCheck) < 0: break;
						if piece != '':
							if not sameCase(kingPiece,piece) and piece.lower() in ('r','q'):
								print('Check!')
								return True
							break
					except IndexError:
						break
		return False

	def checkDiag(center,kingPiece):
		for x in (-1,2):
			for y in (-1,2):
				for tileDelta in range(1,int(sg.boardLength / 2)):
					try:
						tileToCheck = [center[0] + tileDelta * y, center[1] + tileDelta * x]
						piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
						print(piece)
						if min(tileToCheck) < 0: break;
						if piece != '':
							if not sameCase(kingPiece,piece) and piece.lower() in ('b','q'):
								print('Check! (Diagonal)')
								return True
							break
					except IndexError:
						break

	def checkClose(center,kingPiece):
		alreadyChecked = [list(center)]
		print(alreadyChecked)
		for i in range(-1,2):
			for j in range(-1,2):
				tileToCheck = [sg.ia(center[0], i, 0, sg.boardLength - 1),sg.ia(center[1], j, 0, sg.boardLength - 1)]
				if tileToCheck in alreadyChecked: continue
				alreadyChecked.append(tileToCheck)
				piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
				print([i,j],tileToCheck,piece)
				if piece.lower() == 'k':
					print('Check! (Close)')
					return True

	def checkPawn(center,kingPiece):
		def checkItOut(direction):
			for x in (-1,1):
				try:
					tileToCheck = [center[0] + x,center[1] + 1]
					piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
					if not sameCase(piece,kingPiece) and piece.lower() == 'p':
						print('Check! (Pawn)')
						return True
				except IndexError:
					continue

		if sg.isLower(kingPiece):
			#Black can be checked from the front
			checkItOut(1)
		else:
			checkItOut(-1)

	def grumpyHorse(center,kingPiece):
		""" ____________________
			< Quit your meddlin' >
			 --------------------
			   \        \
			    \        \
			     \       _\^
			      \    _- oo\
			           \---- \______
			                 \       )\
			                ||-----||  \
			                ||     ||"""
		def jumpAround(jump):
			for x in (-1,1):
				for y in (-1,1):
					try:
						tileToCheck = [center[0] + jump[0] * x, center[1] + jump[1] * y]
						piece = sg.pieceMatrix[tileToCheck[0]][tileToCheck[1]]
						if not sameCase(piece,kingPiece) and piece.lower() == 'n':
							print('Check! (Knight)')
							return True
					except IndexError:
						continue
		jumpAround([1,2])
		jumpAround([2,1])



	for k in ('k','K'):
		king = getIndexes(k)
		checkStraight(king,k)
		checkDiag(king)
		checkClose(king,k)
		checkPawn(king,k)
		grumpyHorse(king,k)


def checkMate(piece):
	return False

def sameCase(l1,l2):
	return sg.isLower(l1) == sg.isLower(l2)

def sameLetter(l1,l2):
	return l1.lower() == l2.lower()