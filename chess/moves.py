import superGlobals as sg
letters = ['a','b','c','d','e','f','g','h']

def convertMove(move):
	move = str(move)
	vector = []
	if len(move) != 4: return False
	try:
		if move[0] not in letters or move[2] not in letters: return False
		if int(move[1]) not in range(8) or int(move[3]) not in range(8): return False
		
		for i in range(0,4,2):
			vector.append([letters.index(move[i]), int(move[i+1]) - 1])
		return vector
	except ValueError:
		# Second and fourth letter might not int
		return False

def getMove():
	if sg.blackTurn: player = 'Black'
	else: player = 'White'
	move = convertMove(input('{}, your turn: '.format(player)))
	if not move:
		# convertMove() returned False
		print('Input moves like this: c4e6')
		return getMove()
	sg.blackTurn = not sg.blackTurn
	return move