from ajedrez.pieces import Piece

###REYES###
class Kings(Piece):
    
    def __init__(self, color):
        super().__init__(color)

    def movimientos_basicos_de_reyes(self, row, col):

        moves = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    #Le marque las casillas a las que puede ir y luego direc_row recorre las filas y direc_col las columnas
        for direc_row, direc_col in direcciones:#de esta manera se les va agregar la nueva direccion
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:# Verifica que la nueva posición esté dentro del tablero
                moves.append((nueva_fila, nueva_columna))

        return moves


#############