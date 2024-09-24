from ajedrez.pieces import Piece
from ajedrez.totalpieces import DIAGONAL_DIRECCIONES

###ALFILS###
class Alfils(Piece):

    black_str ="♗"
    white_str ="♝"
    direcciones = DIAGONAL_DIRECCIONES
    
    def __init__(self, color):
        super().__init__(color) 

    def valid_moves(self, row, col, board):
        return self.valid_moves_in_directions(row, col, self.direcciones, board)
    
    #Tuve que refacotorizar esta funcion porque era muy larga y de complejidad alta por lo que 
    # era mejor darle las direcciones posibles y que las recorra. 
    