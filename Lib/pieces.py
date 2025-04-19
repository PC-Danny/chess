from utils import isPosition
chess_pieces = [
    'white_king', 
    'white_queen', 
    'white_knight1', 'white_knight2', 
    'white_bishop1', 'white_bishop2',
    'white_rook1', 'white_rook2', 
    'white_pawn1','white_pawn2','white_pawn3','white_pawn4','white_pawn5','white_pawn6','white_pawn7','white_pawn8',
    'black_king', 
    'black_queen', 
    'black_knight1', 'black_knight2', 
    'black_bishop1','black_bishop2',
    'black_rook1', 'black_rook2', 
    'black_pawn1','black_pawn2','black_pawn3','black_pawn4','black_pawn5','black_pawn6','black_pawn7','black_pawn8']

chess_colours = ['white', 'black']

class Piece: #TODO alle children van Piece moeten een chess icoon hebben in een variabel piece. 
    status = 'unmoved'

    moveLambdas = [lambda i: i[0] == 0 and i[1] > 0, 
         lambda i: i[0] == i[1] and i[1] > 0 , 
         lambda i: i[0] > 0 and i[1] == 0, 
         lambda i: abs(i[0]) == abs(i[1]) and i[0] > 0 and i[1] < 0, 
         lambda i: i[0] == 0 and i[1] < 0, 
         lambda i: i[0] == i[1] and i[1] < 0, 
         lambda i: i[0] < 0 and i[1] == 0, 
         lambda i: abs(i[0]) == abs(i[1]) and i[0] < 0 and i[1] > 0]

    directionVectors = ['movesN',
                        'movesNE',
                        'movesE',
                        'movesSE',
                        'movesS',
                        'movesSW',
                        'movesW',
                        'movesNW']
    
    def __init__(self, gridPosition, colour: str, piece: str, name:str = 'temp' , status = 'unmoved',):
        self.piece = piece
        self.colour = colour
        self.gridPosition = gridPosition
        self.name = name
        self.status = status
        self.oppositeColour = 'white' if colour == 'black' else 'black'
        pass
    def __str__(self):
        return f"'tis a {self.colour} {self.piece}..."
    
    def moves(self,moveRange: range = []) -> list[tuple[int,int]]:
        moves = []
        for x in moveRange:
            for y in moveRange:
                moves.append((x,y))
        if (0,0) in moves:
            moves.remove((0,0))
        return moves


            
    def castle(self):
        pass

    def die(self):
        globals()[f"conquered{(self.colour).capitalize()}Pieces"].append(self.name)
        self.status = 'defeated'    

class King(Piece):
    def moves(self, rooks, moveRange = range(-1,2)):
        # TODO include castling move
        moves = super().moves(moveRange)
        if (self.status=='unmoved'):
            for r in rooks:
                if r.status == 'unmoved':
                    moves + [r.gridPosition]
        return moves

class Queen(Piece):
    def moves(self, moveRange = range(-7,8)):
        return [m for m in super().moves(moveRange) if 0 in m]+[m for m in super().moves(moveRange) if (not 0 in m) and (abs(m[0])==abs(m[1]))]
    
class Rook(Piece):
    def moves(self, moveRange = range(-7,8)):
        # include castling move
        return [m for m in super().moves(moveRange) if 0 in m]

class Bishop(Piece):
    def moves(self, moveRange = range(-7,8)):
        print([m for m in super().moves(moveRange) if (not 0 in m) and (abs(m[0])==abs(m[1]))])
        return [m for m in super().moves(moveRange) if (not 0 in m) and (abs(m[0])==abs(m[1]))]

class Knight(Piece):
    def moves(self):
        #TODO knights links onder en links boven kunnen niet naar links bewegen.
        return [[dx * x, dy * y] for x, y in [[1, 2], [2, 1]] for dx in [-1, 1] for dy in [-1, 1]]
    
class Pawn(Piece):
    def moves(self,cellList):
        x = self.gridPosition[0]
        y = self.gridPosition[1]        
        
        moves = [[0,1]]
        if self.status == 'unmoved':
            moves.append([0,2])

        if self.colour == 'black':
            moves = [[m[0],m[1]*-1] for m in moves]
        
        
        try:
            if cellList.get(f'cell{x - moves[0][0]}_{y - moves[0][1]}').piece:
                moves=[]
        except:
            pass
        moves += self.checkDiagonal(cellList, x, y)
        print(moves)
        return moves
    
    def checkDiagonal(self, cellList, x, y) -> bool:
        diagonals = [[-1,1],[1,1]] if self.colour == 'white' else [[-1, -1], [1,-1]]
        # diagonals = [[x--1,y-1],[x-1,y-1]] if self.colour == 'white' else [[x--1, y--1], [x-1,y--1]]
        diagonalMoves = []
        print('the diagonals are:',diagonals)
        for d in diagonals:
            pos = [x - d[0],y - d[1]]
            print('*')
            try:
                isPosition(pos)
                print(cellList.get(f'cell{pos[0]}_{pos[1]}').piece)
                if cellList.get(f'cell{pos[0]}_{pos[1]}').piece.colour == self.oppositeColour:
                    diagonalMoves.append(d)
                    print('*1')
                else:
                    print('*2')
            except Exception as e:
                print('#')
                print(e)
                pass
        print('the diagonal moves are:',diagonalMoves)
        return diagonalMoves
        # return [d for d in diagonals if globals()[f'cell{self.gridd[0]}_{d[1]}'].piece.colour == chess_colours.remove(self.colour)[0]]
        
    

    
    def promotion(self):
        pass


if __name__ == "__main__":
    list = ['Knight', 'Pawn', 'Queen', 'Rook', 'Knight', 'Bishop']
    piece = Queen(1,'black', 'c')
    print(piece.moves())