from ajedrez.pieces import Piece

###CABALLOS###
class Horse(Piece):

    black_str ="♘" #knight black
    white_str ="♞"  #knight white
    direcciones = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    #No se me complico hacer el codigo de los movimientos del caballo porque 
    # sigue el formato de los Reyes con la diferencia que las casillas que ocupa son diferentes
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, row, col, board):

        moves = []

        for direc_row, direc_col in self.direcciones:
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                if not self.validar_colision(nueva_fila, nueva_columna, board):
                        moves.append((nueva_fila, nueva_columna))

        return moves
    
#############