from tkinter import *
from PIL import Image
import moves
import superGlobals as sg

# Variables
backgroundColor = "#eeeeee"
tileColor = "#222222"
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
			photo = PhotoImage(file='img46/{}.gif'.format(piece))
			#w.photo = photo
			w.photos[i].append(photo)
			w.create_image(tileWidth * j, tileWidth * i, anchor=NW, image=w.photos[i][j])

drawPieces(sg.pieceMatrix)

def main():
	while True:
		move = moves.getMove()
		print(move)
		#drawPieces("kek")
		#w.create_rectangle(300,200,310,210,fill="#ff0000")

master.after(0,main())

mainloop()