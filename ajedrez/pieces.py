class Piece:    #Clase Padre
    def __init__(self, color):
        self.__color__ = color

    @property#Me toma como objeto privado el color entonces vi que si hago @property lo solucionaba
    
    def color(self):
        return self.__color__
    
    def __str__ (self):

        if self.__color__ == "BLACK":
            return self.black_str
        else:
            return self.white_str
            
#############USADO PARA TODAS LAS PIEZAS#################

    def validar_colision(self, row, col, board):
        # Verifica si hay colisión con una pieza del mismo color en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ == self.__color__

    def validar_captura(self, row, col, board):
        # Verifica si la pieza puede capturar una pieza enemiga en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ != self.__color__
    
    ##########USADO PARA ALFILS Y ROOK##############

    def valid_moves_in_directions(self, row, col, direcciones, board):
        moves = []
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