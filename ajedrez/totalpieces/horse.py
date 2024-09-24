from ajedrez.pieces import Piece
from ajedrez.totalpieces import HORSES_MOVEMENTS

###CABALLOS###
class Horse(Piece):

    black_str ="♘" #knight black
    white_str ="♞"  #knight white
    direcciones = HORSES_MOVEMENTS
    
    #No se me complico hacer el codigo de los movimientos del caballo porque 
    # sigue el formato de los Reyes con la diferencia que las casillas que ocupa son diferentes

    def valid_moves(self, row, col, board):

        moves = []

        for direc_row, direc_col in self.direcciones:
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                if not self.validar_colision(nueva_fila, nueva_columna, board):
                        moves.append((nueva_fila, nueva_columna))

        return moves
    
#############