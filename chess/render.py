from tkinter import *

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

#Order
#w.create_rectangle(x0,y0,x1,x1)

#Draw tiles
def drawTiles():
	for i in range(boardLength):
		for j in range(boardLength):
			# If sum of indexes are even, the tile is white
			# This applies only if the board is of even size

			# It's probably the opposite if it's odd sized tho, so 
			# with a second condition this could be solved easily
			# I just don't really care enough
			print((j + i) % 2)
			if (j + i) % 2 != 0:
				w.create_rectangle(j * tileWidth, i * tileHeight, j * tileWidth + tileWidth, i * tileHeight + tileHeight, fill=tileColor, outline=tileColor)

drawTiles()
pieceMatrix = [['r','B','q'],['p','P','K']]
def drawPieces(pieceMatrix):
	# Just to show photo implementation
	photo = PhotoImage(file='p.png')
	print(photo)
	w.create_image(40, 40, image = photo, anchor = NW)


def main():
	while True:
		input("say somthn ")
		drawPieces("kek")
		#w.create_rectangle(300,200,310,210,fill="#ff0000")

master.after(0,main())

mainloop()