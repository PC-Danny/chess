import numpy as np
import tkinter as tk
from Lib.pieces import Piece, King, Queen, Knight, Rook, Bishop, Pawn, chess_pieces

horizontal_positions = ['a','b','c','d','e','f','g','h']
vertical_positions = [8,7,6,5,4,3,2,1]
turn = 'white'
# moveState = 1 wanneer je op een knop wilt drukken om deze te bewegen, dan verandert deze naar 0 om op een highlighted knop te drukken om hierheen te verplaatsen.
moveState = 1
movedPiece = None
possibleCellsList = []

def chessNotation():
    pass
    #TODO Deze functie geeft de moves die zijn gemaakt door in een algebraïsche schaak notatie.

def translatePosition(pos:tuple):
    return f"{chr(pos[0]+96)}{vertical_positions[pos[1]-1]}"

def checkmate(king):
    #! dit is een fictieve code
    possibleMovesOpponent = []
    for p in opposingPieces:
        possibleMovesOpponent.append(p.moves())
    if king.gridPosition in possibleMovesOpponent:
        return 'checkmate' if set(king.moves).issubset(possibleMovesOpponent) else 'check' 

class Cell(tk.Button):
    # super().bg = 'black'
    def __init__(self,gridPosition: tuple[int,int], piece: Piece = None,*args, **kwargs):
        tk.Button.__init__(self, command = self.buttonClicked, *args, **kwargs)
        self.gridPosition = gridPosition
        self.piece = piece
        pass
    
    def changeText(self):
        self.text = 'changed'


    def buttonClicked(self):
        global turn
        global cells
        global moveState
        global movedPiece 
        if moveState:
            if self.piece.colour != turn:
                color = self['bg']
                self.config(bg="red")
                self.update_idletasks()
                self.after(1000, self.config(bg=color))
                print('wrong colour')
            else:
                moveState = 0
                movedPiece = self.movePiece()

        else:
            if self in possibleCellsList:
            # movedPiece is het schaakstuk dat
                self.piece = movedPiece
                self.config(text = movedPiece.name)
                moveState = 1
            else: pass
        

    def movePiece(self):
        global turn
        global cells
        global possibleCellsList


        moves = [move for move in self.piece.moves()]
        # moves = [translatePosition(move) for move in self.piece.moves()]
        print(moves)
        print(self.gridPosition)
        print(self.piece.gridPosition)
        possibleCells = [np.array(self.piece.gridPosition) - np.array(move) for move in moves if 
                         (np.array(self.piece.gridPosition) - np.array(move))[0] >= 1 and
                         (np.array(self.piece.gridPosition) - np.array(move))[1] >= 1 and
                         (np.array(self.piece.gridPosition) - np.array(move))[0] <= 8 and
                         (np.array(self.piece.gridPosition) - np.array(move))[1] <= 8]
        print(possibleCells)
        for x in possibleCells:
            cell = globals()[f"cell{x[0]}_{x[1]}"]
            cell.config(bg="white")
            possibleCellsList.append(cell)


        turn = 'white' if turn =='black' else 'black'
        return self.piece
        
    # tk.Button.bind()  

def startGame():
    conqueredBlackPieces = []
    conqueredWhitePieces = []

    window = tk.Tk()
    frame = tk.Frame()

    colours = ['white', 'black']
    #Setting up the pieces
    for c in colours:
        if c == 'white':
            ypos1 = 8
            ypos2 = 7
        else:
            ypos1 = 1
            ypos2 = 2
        
        globals()[f"{c}_king"] = King([5,ypos1], c, 'King', name = f'{c} {'King'}')
        globals()[f"{c}_queen"] = Queen([4,ypos1], c, 'Queen', name = f'{c} {'Queen'}')
        globals()[f"{c}_rook1"] = Rook([1,ypos1], c, 'Rook', name = f'{c} {'Rook'}')
        globals()[f"{c}_rook2"] = Rook([8,ypos1], c, 'Rook', name = f'{c} {'Rook'}')
        globals()[f"{c}_knight1"] = Knight([2,ypos1], c, 'Knight', name = f'{c} {'Knight'}')
        globals()[f"{c}_knight2"] = Knight([7,ypos1], c, 'Knight', name = f'{c} {'Knight'}')
        globals()[f"{c}_bishop1"] = Bishop([3,ypos1], c, 'Bishop', name = f'{c} {'Bishop'}')
        globals()[f"{c}_bishop2"] = Bishop([6,ypos1], c, 'Bishop', name = f'{c} {'Bishop'}')

        for i in range(1,9):
            globals()[f"{c}_pawn{i}"] = Pawn([i,ypos2], c, 'Pawn')

    #Setting up the chess grid
    global cells
    cells = []
    for y in range(1,9):
        for x in range(1,9):

            piece = next((globals()[f"{p}"] for p in chess_pieces if globals()[f"{p}"].gridPosition == [x,y]), None)
            # print(x,y,piece)

            globals()[f"cell{x}_{y}"] = Cell(gridPosition = (x,y), piece = piece, text = f'{piece.colour} {piece.piece}' if piece else '', width = 9, height = 3, master=frame)
            globals()[f"cell{x}_{y}"].grid(row = y, column = x)
            cells.append(globals()[f"cell{x}_{y}"])

    frame.pack()

    print(black_rook1.status)

    window.mainloop()

startGame()