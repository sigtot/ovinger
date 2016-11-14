from tkinter import *
from PIL import Image
import moves
import superGlobals as sg

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

def performMove(move):
	# Remember [X,Y] in move corresponds to [Y][X] in matrix
	# target = piece
	sg.pieceMatrix[move[1][1]][move[1][0]] = sg.pieceMatrix[move[0][1]][move[0][0]]
	#piece = ''
	sg.pieceMatrix[move[0][1]][move[0][0]] = ''
	sg.blackTurn = not sg.blackTurn

drawPieces(sg.pieceMatrix)
def main():
	move = moves.getMove()
	performMove(move)
	drawPieces(sg.pieceMatrix)
	master.after(0,main())

master.after(0,main())

mainloop()