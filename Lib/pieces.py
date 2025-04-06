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


class Piece: #TODO alle children van Piece moeten een chess icoon hebben in een variabel piece. 
    status = 'unmoved'
    def __init__(self, gridPosition, colour: str, piece: str, name:str = 'temp' , status = 'unmoved',):
        self.piece = piece
        self.colour = colour
        self.gridPosition = gridPosition
        self.name = name
        self.status = status
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
    def moves(self, moveRange = range(-1,2)):
        # TODO include castling move
        if (self.status=='unmoved'):
            rook = globals()[f"{self.colour}_rook1"]
            if rook.status == 'unmoved':
                pass 
        return super().moves(moveRange)

class Queen(Piece):
    @classmethod
    def moves(self, moveRange = range(-7,8)):
        # return super().moves(moveRange)
        return [m for m in super().moves(moveRange) if 0 in m].append([m for m in super().moves(moveRange) if not 0 in m])
    
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