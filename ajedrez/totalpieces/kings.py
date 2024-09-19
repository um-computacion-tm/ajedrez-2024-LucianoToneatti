from ajedrez.pieces import Piece

###REYES###
class Kings(Piece):
    
    black_str ="♔"
    white_str ="♚"
    

    def __init__(self, color):
        super().__init__(color)

    def validar_colision(self, row, col, board):
        #Verifica si hay colisión con una pieza del mismo color en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ == self.__color__

    def validar_captura(self, row, col, board):
        #Verifica si la torre puede capturar una pieza enemiga en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ != self.__color__


    def valid_moves(self, row, col, board):

        moves = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    #Le marque las casillas a las que puede ir y luego direc_row recorre las filas y direc_col las columnas
        for direc_row, direc_col in direcciones:#de esta manera se les va agregar la nueva direccion
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:# Verifica que la nueva posición esté dentro del tablero
                if not self.validar_colision(nueva_fila, nueva_columna, board):# Verifica si hay una pieza en la nueva ubicación
                    if self.validar_captura(nueva_fila, nueva_columna, board):
                        moves.append((nueva_fila, nueva_columna))
                    else:
                        moves.append((nueva_fila, nueva_columna))

        return moves

#############