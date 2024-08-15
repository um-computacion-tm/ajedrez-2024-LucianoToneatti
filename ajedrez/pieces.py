class Piece:    #Clase Padre
    def __init__(self, color):
        self.__color__ = color

    @property             #Me toma como objeto privado el color entonces vi que si hago @property lo solucionaba
    
    def color(self):
        return self.__color__

class Rook(Piece):     #Piezas de Torre
    def __init__(self, color):
        super().__init__(color) 


class Pawn(Piece):     #Piezas de Peon
    pass