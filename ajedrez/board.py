from ajedrez.pieces import Rook
from ajedrez.pieces import Pawn
from ajedrez.pieces import Queen
from ajedrez.pieces import Knight
from ajedrez.pieces import Horse
from ajedrez.pieces import Alfils
class Board:

    def __init__(self): # Crear un tablero de 8x8 
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #Le damos posiciones a las Torres Black y White#   

        self.__positions__[0][0] = Rook("BLACK") #Black
        self.__positions__[0][7] = Rook("BLACK") #Black
        self.__positions__[7][7] = Rook("WHITE") #White 
        self.__positions__[7][0] = Rook("WHITE") #White


        #Le damos posiciones a los Alfiles negros y blancos#

        self.__positions__[0][1] = Alfils("BLACK") #Black
        self.__positions__[0][6] = Alfils("BLACK") #Black
        self.__positions__[7][1] = Alfils("WHITE") #White 
        self.__positions__[7][6] = Alfils("WHITE") #White

        #Le damos posiciones a los Caballos negros y blancos#

        self.__positions__[0][2] = Horse("BLACK") #Black
        self.__positions__[0][5] = Horse("BLACK") #Black
        self.__positions__[7][2] = Horse("WHITE") #White 
        self.__positions__[7][5] = Horse("WHITE") #White

        #Le damos posiciones a los Peones negros y blancos#

        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK") #Black
            self.__positions__[6][i] = Pawn("WHITE") #White


        #Le damos posiciones a las Reinas negras y blancas#

        self.__positions__[0][3] = Queen("BLACK") #Black
        self.__positions__[7][3] = Queen("WHITE") #White

        #Le damos posiciones a los Reyes negros y blancos#

        self.__positions__[0][4] = Knight("BLACK") #Black
        self.__positions__[7][4] = Knight("WHITE") #White


    #Sirve para obtener la pieza
    
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    #Sirve para obtener los movimientos de las torres para luego usarlos en el tablero

    def get_rook_moves(self, row, col): 
        rook = self.get_piece(row, col)
        if isinstance(rook, Rook):
            return rook.movimientos_basicos_de_torres(row, col)
        else:
            return []
        
    #Sirve para obtener los movimientos de los alfiles para luego usarlos en el tablero

    def get_alfils_moves(self, row, col):
        alfil = self.get_piece(row, col)
        if isinstance(alfil, Alfils):
            return alfil.movimientos_basicos_de_alfiles(row, col)
        else:
            return []
    
    #Sirve para obtener los movimientos de los caballos para luego usarlos en el tablero
    def get_Queen_moves(self, row, col):
        queen = self.get_piece(row, col)
        if isinstance(queen, Queen):
            return queen.movimientos_basicos_de_reinas(row, col)
        else:
            return []


        #Todavia no implemento la colicion de piezas