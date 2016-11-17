from tkinter import *
from PIL import Image
import moves
import superGlobals as sg
import check

import sys
sys.setrecursionlimit(10000000) # YES RECURSION

# Variables
backgroundColor = '#ffce9e' #"#eeeeee"
tileColor = '#d18b47' #"#222222"
canvasHeight = 400
canvasWidth = 400
boardLength = 8

tileWidth = int(canvasWidth / boardLength)
tileHeight = int(canvasHeight / boardLength)

master = Tk()
w = Canvas(master, width=canvasWidth, height=canvasHeight, bg=backgroundColor, highlightthickness=0)
w.pack()

#Draw tiles
def drawTiles():
	for i in range(boardLength):
		for j in range(boardLength):
			# If sum of indexes are even, the tile is white
			# This applies only if the board is of even size

			# It's probably the opposite if it's odd sized tho, so 
			# with a second condition this could be solved easily
			# I just don't really care enough
			if (j + i) % 2 != 0:
				w.create_rectangle(j * tileWidth, i * tileHeight, j * tileWidth + tileWidth, i * tileHeight + tileHeight, fill=tileColor, outline=tileColor)

drawTiles()
def drawPieces(pieceMatrix):
	w.photos = []
	for i,row in enumerate(pieceMatrix):
		w.photos.append([])
		for j,piece in enumerate(row):
			# æsj
			if piece == '': photo = ''
			else: photo = PhotoImage(file='img46/{}.gif'.format(piece))
			w.photos[i].append(photo)

			if piece != '':
				w.create_image(tileWidth * j, tileWidth * i, anchor=NW, image=w.photos[i][j])

drawPieces(sg.pieceMatrix)
def main():
	move = moves.getMove()
	if sg.getCheck():
		old = moves.performMove(move,True)
		if sg.blackTurn: 
			king = check.getIndexes('k')
			k = 'k'
		else: 
			king = check.getIndexes('K')
			k = 'K'
		if check.check(True,king,k):
			print('You\'re in check')
			# Revert move
			moves.performMove(move[::-1],True)
			sg.pieceMatrix[move[1][1]][move[1][0]] = old
		else:
			check.setCheck(False)
	else:
		check.setCheck(False)
		old = moves.performMove(move,True)
		# If after the move, you're now in check: revert the move
		if sg.blackTurn: 
			king = check.getIndexes('k')
			k = 'k'
		else: 
			king = check.getIndexes('K')
			k = 'K'
			# At this point I'm really just copy pasting stuff
			# But fuck it i'm done with this shit
		if check.check(True,king,k):
			moves.performMove(move[::-1],True)
			sg.pieceMatrix[move[0][1]][move[0][0]] = old
			sg.blackTurn = not sg.blackTurn
			print('You\'re putting yourself into check')

	drawPieces(sg.pieceMatrix)
	if check.check():
		print('Check!')
		check.setCheck(True)
	sg.blackTurn = not sg.blackTurn
	master.after(0,main())

master.after(0,main())

mainloop()