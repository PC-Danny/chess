import tkinter as tk
from Lib.pieces import Piece, King, Queen, Knight, Rook, Bishop, Pawn, chess_pieces

horizontal_positions = ['a','b','c','d','e','f','g','h']
vertical_positions = [1,2,3,4,5,6,7,8]

def chessNotation():
    pass
    #TODO Deze functie geeft de moves die zijn gemaakt door in een algebraïsche schaak notatie.

def translatePosition(pos):
    return f"{chr(pos[0]+96)}{pos[1]}"

def checkmate(king):
    #! dit is een fictieve code
    possibleMovesOpponent = []
    for p in opposingPieces:
        possibleMovesOpponent.append(p.moves())
    if king.position in possibleMovesOpponent:
        return 'checkmate' if set(king.moves).issubset(possibleMovesOpponent) else 'check' 

class Cell(tk.Button):
    # super().bg = 'black'
    def __init__(self,position,status = None,*args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.position = position
        self.status = status
        pass
    
    def changeText(self):
        self.text = 'changed'
        
    # tk.Button.bind()  

def startGame():
    conqueredBlackPieces = []
    conqueredWhitePieces = []

    window = tk.Tk()
    frame = tk.Frame()

    colours = ['white', 'black']
    #Setting up the pieces
    for c in colours:
        if c == 'black':
            ypos1 = 8
            ypos2 = 7
        else:
            ypos1 = 1
            ypos2 = 2
        
        globals()[f"{c}_king"] = King([ypos1,5], c, 'King')
        globals()[f"{c}_queen"] = Queen([ypos1, 4], c, 'Queen')
        globals()[f"{c}_rook1"] = Rook([ypos1,1], c, 'Rook')
        globals()[f"{c}_rook2"] = Rook([ypos1,8], c, 'Rook')
        globals()[f"{c}_knight1"] = Knight([ypos1,2], c, 'Knight')
        globals()[f"{c}_knight2"] = Knight([ypos1,7], c, 'Knight')
        globals()[f"{c}_bishop1"] = Bishop([ypos1,3], c, 'Bishop')
        globals()[f"{c}_bishop2"] = Bishop([ypos1,6], c, 'Bishop')

        for i in range(1,9):
            globals()[f"{c}_pawn{i}"] = Pawn([ypos2,i], c, 'Pawn')

    #Setting up the chess grid
    global cells
    cells = []
    for x in range(1,9):
        for y in range(1,9):

            piece = next((globals()[f"{p}"] for p in chess_pieces if globals()[f"{p}"].position == [x,y]), None)
            print(x,y,piece)

            globals()[f"cell{x}_{y}"] = Cell(position=translatePosition([x,y]),status=piece, text= f'{piece.colour} {piece.piece}' if piece else '', width = 9, height = 3, master=frame)
            globals()[f"cell{x}_{y}"].grid(column = y, row = x)
            cells.append(globals()[f"cell{x}_{y}"])

    frame.pack()

    window.mainloop()

startGame()