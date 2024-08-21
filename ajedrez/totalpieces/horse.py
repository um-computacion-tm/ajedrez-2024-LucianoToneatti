from ajedrez.pieces import Piece

###CABALLOS###
class Horse(Piece):
    #No se me complico hacer el codigo de los movimientos del caballo porque 
    # sigue el formato de los Reyes con la diferencia que las casillas que ocupa son diferentes
    def __init__(self, color):
        super().__init__(color)
    
    def movimientos_basicos_de_caballos(self, row, col):

        moves = []
        direcciones = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for direc_row, direc_col in direcciones:
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                moves.append((nueva_fila, nueva_columna))

        return moves
    
#############