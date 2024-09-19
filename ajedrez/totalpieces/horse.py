from ajedrez.pieces import Piece

###CABALLOS###
class Horse(Piece):

    black_str ="♘" #knight black
    white_str ="♞"  #knight white
    
    #No se me complico hacer el codigo de los movimientos del caballo porque 
    # sigue el formato de los Reyes con la diferencia que las casillas que ocupa son diferentes
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
        direcciones = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for direc_row, direc_col in direcciones:
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                if not self.validar_colision(nueva_fila, nueva_columna, board):
                        moves.append((nueva_fila, nueva_columna))

        return moves
    
#############