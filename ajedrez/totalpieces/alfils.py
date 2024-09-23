from ajedrez.pieces import Piece

###ALFILS###
class Alfils(Piece):

    black_str ="♗"
    white_str ="♝"
    
    
    def __init__(self, color):
        super().__init__(color) 

    def valid_moves(self, row, col, board):
        moves = []
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for direc_row, direc_col in direcciones:
            moves.extend(self.valid_moves_in_direction(row, col, direc_row, direc_col, board))
        return moves
    
    #Tuve que refacotorizar esta funcion porque era muy larga y de complejidad alta por lo que 
    # era mejor darle las direcciones posibles y que las recorra. 
    