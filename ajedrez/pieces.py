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
            
#############

    def validar_colision(self, row, col, board):
        # Verifica si hay colisión con una pieza del mismo color en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ == self.__color__

    def validar_captura(self, row, col, board):
        # Verifica si la pieza puede capturar una pieza enemiga en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ != self.__color__