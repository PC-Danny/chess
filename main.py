horizontal_positions = [1,2,3,4,5,6,7,8]
vertical_positions = ['a','b','c','d','e','f','g','h']

def translatePosition(pos):
    return f"{chr(pos[0]+96)}{pos[1]}"

def checkmate(king):
    #! dit is een fictieve code
    possibleMovesOpponent = []
    for p in opposingPieces:
        possibleMovesOpponent.append(p.moves())
    if king.position in possibleMovesOpponent:
        return 'checkmate' if set(king.moves).issubset(possibleMovesOpponent) else 'check' 
 

conqueredBlackPieces = []
conqueredWhitePieces = []

class Cell:
    def __init__(self,position,status):
        self.position = position
        self.status = status
        pass

class Piece:
    piece = ''
    def __init__(self,position, colour, name, status = 'unmoved'):
        self.colour = colour
        self.position = position
        self.name = name
        self.status = status
        pass
    def __str__(self):
        return f"'tis a {self.colour} {self.piece}..."
    
    def moves(self,moveRange = []):
        moves = []
        for x in moveRange:
            for y in moveRange:
                moves.append([x,y])
        moves.remove([0,0])
        return moves
    def castle(self):
        pass

    def die(self):
        globals()[f"conquered{(self.colour).capitalize()}Pieces"].append(self.name)
        self.status = 'defeated'    

class King(Piece):
    def moves(self,moveRange = range(-1,2)):
        # include castling move
        if (self.status=='unmoved'):
            if globals()[f"{self.colour}_rook1"] == 'unmoved':
                pass 
        return super().moves(moveRange)

class Queen(Piece):
    def moves(self, moveRange = range(-7,8)):
        # return super().moves(moveRange)
        return [m for m in super().moves(moveRange) if 0 in m].append([m for m in super().moves(moveRange) if not 0 in m])
    

class Rook(Piece):
    def moves(self, moveRange = range(-7,8)):
        # include castling move
        return [m for m in super().moves(moveRange) if 0 in m]

class Bishop(Piece):
    def moves(self, moveRange = range(-7,8)):
        return [m for m in super().moves(moveRange) if not 0 in m]

class Knight(Piece):
    def moves():
        return [[dx * x, dy * y] for x, y in [[1, 2], [2, 1]] for dx in [-1, 1] for dy in [-1, 1]]
    
class Pawn(Piece):
    def moves(self):
        if self.status == 'unmoved':
            x = 0
            if self.colour == 'black':
                return [[x,-1],[x,-2]]
            else:
                return [[x,1],[x,2]]
    
    def promotion(self):
        pass

    

def startGame():


    colours = ['white', 'black']

    for c in colours:
        globals()[f"{c}_king"] = King('e8', c)
        globals()[f"{c}_queen"] = Queen('e8', c)
        for i in range(2):
            globals()[f"{c}_{i+1}"] = ''

startGame()

def test():
    test = Bishop(1,2)
    test.moves()

test()