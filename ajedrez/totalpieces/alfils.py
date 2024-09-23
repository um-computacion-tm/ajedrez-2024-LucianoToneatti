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
            r, c = row + direc_row, col + direc_col
            while 0 <= r < 8 and 0 <= c < 8:
                if self.validar_colision(r, c, board):
                    break
                if self.validar_captura(r, c, board):
                    moves.append((r, c))
                    break
                moves.append((r, c))
                r += direc_row
                c += direc_col
        return moves
    
    #Tuve que refacotorizar esta funcion porque era muy larga y de complejidad alta por lo que 
    # era mejor darle las direcciones posibles y que las recorra. 
    