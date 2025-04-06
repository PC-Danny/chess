
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Lib.pieces    import Piece, King, Queen, Knight, Rook, Bishop, Pawn, chess_pieces

# king = King()
test = Queen.moves()
print(test)