import math
def makeBoard(bs):
	if int(math.sqrt(len(bs))) != math.sqrt(len(bs)):
		print('Non square board')
		return


boardString = 'rkn.r.p.....P..PP.PPB.K..'
board = makeBoard(boardString)
