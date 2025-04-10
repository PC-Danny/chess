import numpy as np
import tkinter as tk
from Lib.pieces import Piece, King, Queen, Knight, Rook, Bishop, Pawn, chess_pieces
from utils import sqdist, isPosition

horizontal_positions = ['a','b','c','d','e','f','g','h']
vertical_positions = [8,7,6,5,4,3,2,1]
turn = 'white'
# moveState = 1 wanneer je op een knop wilt drukken om deze te bewegen, dan verandert deze naar 0 om op een highlighted knop te drukken om hierheen te verplaatsen.
moveState = 1
movedPiece = None
possibleCellsList = []
currentCell = None

def showPossibleMoves():
    global possibleCellsList
    for cell in possibleCellsList:
        if cell['bg'] == 'white':
            cell.config(bg = 'grey')
        else:
            cell.config(bg='white')



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
    def __init__(self,gridPosition: list[int,int], piece: Piece = None,*args, **kwargs):
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
        global currentCell
        global possibleCellsList
        if moveState or (currentCell != None and currentCell != self and self.piece != None and self.piece.colour == currentCell.piece.colour):
            if self.piece and self.piece.colour != turn:
                color = self['bg']
                self.config(bg="red")
                self.update_idletasks()
                self.after(1000, self.config(bg=color))
                print('wrong colour')
            elif not self.piece:
                print('empty')
            else:
                # print(self.piece.moves())
                possibleCellsList = []
                movedPiece = self.movePiece()
                currentCell = self
                # conditie dat als geen mogelijke moves, dan geen movestate veranderen... en dus ook geen turn vernanderen 
                # TODO kijken waar turn moet veranderen
                moveState = 0

        else:
            if self in possibleCellsList:
            # movedPiece is het schaakstuk dat
                self.piece = movedPiece
                self.piece.status = 'moved'
                self.piece.gridPosition = self.gridPosition
                self.config(text = movedPiece.name)

                # Het opschonen van cell waarvan het stuk beweegt.
                currentCell.config(text="")
                currentCell.piece = None
                currentCell = None
                
                showPossibleMoves()
                possibleCellsList = []
                moveState = 1
                turn = 'white' if turn =='black' else 'black'
            elif self == currentCell:
                moveState = 1
                print('well done')
                
            else: 
                pass
        
    def checkPossibility(self, newCell):
        """
        Deze functie bekijkt welke zetten er mogelijk zijn van een schaakstuk
        """
        
        # cell = globals()[f"cell{pos[0]}_{pos[1]}"]
        if newCell.piece:
            if self.piece.colour == newCell.piece.colour:
                raise Exception()
            else:
                possibleCellsList.append(newCell)
                raise Exception()
        else:
            possibleCellsList.append(newCell)

    def movePiece(self):
        """
        Functie die wordt uitgevoerd als het mogelijk is voo
        """
        global turn
        global cells
        global possibleCellsList
        
        if isinstance(self.piece, King):
            rooks = [globals()[f'{self.piece.colour}_rook{i}'] for i in [1,2]]
            moves = [move for move in self.piece.moves(rooks)]
        else:
            moves = [move for move in self.piece.moves()]
        

        # print(moves)
        # print(self.gridPosition)
        # print(self.piece.gridPosition)
        
        # Een loop door de mogelijke nieuwe posities. Stopt mogelijk nieuwe cellen van de piece in een lijst [possibleCellsList].
        if isinstance(self.piece, (King, Knight,Pawn)):
            for move in moves:
                newPosition = np.array(self.piece.gridPosition) - np.array(move)
                try:
                    newCell = globals()[f"cell{newPosition[0]}_{newPosition[1]}"]
                    self.checkPossibility(newCell)
                except:
                    pass
        else:
            for d,l in zip(self.piece.directionVectors,self.piece.moveLambdas):
                direction = [m for m in moves if l(m)]
                direction.sort(key=sqdist)
                for step in direction:
                    newPosition = np.array(self.piece.gridPosition) - np.array(step)
                    try:
                        isPosition(newPosition)
                        newCell = globals()[f"cell{newPosition[0]}_{newPosition[1]}"]
                        self.checkPossibility(newCell)
                    except:
                        break                    

        showPossibleMoves()


        
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
            globals()[f"{c}_pawn{i}"] = Pawn([i,ypos2], c, 'Pawn', name = f'{c} {'Pawn'}')

    #Setting up the chess grid
    global cells
    cells = []
    for y in range(1,9):
        for x in range(1,9):

            piece = next((globals()[f"{p}"] for p in chess_pieces if globals()[f"{p}"].gridPosition == [x,y]), None)
            # print(x,y,piece)

            globals()[f"cell{x}_{y}"] = Cell(gridPosition = [x,y], piece = piece, text = f'{piece.colour} {piece.piece}' if piece else '', width = 9, height = 3, master=frame)
            globals()[f"cell{x}_{y}"].grid(row = y, column = x)
            cells.append(globals()[f"cell{x}_{y}"])

    frame.pack()

    window.mainloop()

startGame()