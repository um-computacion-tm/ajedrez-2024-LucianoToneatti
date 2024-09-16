from ajedrez.totalpieces.rook import Rook
from ajedrez.totalpieces.pawn import Pawn
from ajedrez.totalpieces.queens import Queen
from ajedrez.totalpieces.kings import Kings
from ajedrez.totalpieces.horse import Horse
from ajedrez.totalpieces.alfils import Alfils

from ajedrez.exceptions import OutOfBoard

class Board:

    def __init__(self, for_test = False): # Crear un tablero de 8x8 
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:

        #Le damos posiciones a las Torres Black y White#   

            self.__positions__[0][0] = Rook("BLACK") #Black
            self.__positions__[0][7] = Rook("BLACK") #Black
            self.__positions__[7][7] = Rook("WHITE") #White 
            self.__positions__[7][0] = Rook("WHITE") #White


        #Le damos posiciones a los Caballos negros y blancos#

            self.__positions__[0][1] = Horse("BLACK") #Black
            self.__positions__[0][6] = Horse("BLACK") #Black
            self.__positions__[7][1] = Horse("WHITE") #White 
            self.__positions__[7][6] = Horse("WHITE") #White

        #Le damos posiciones a los Alfiles negros y blancos#

            self.__positions__[0][2] = Alfils("BLACK") #Black
            self.__positions__[0][5] = Alfils("BLACK") #Black
            self.__positions__[7][2] = Alfils("WHITE") #White 
            self.__positions__[7][5] = Alfils("WHITE") #White

        #Le damos posiciones a los Peones negros y blancos#

            for i in range(8):
                self.__positions__[1][i] = Pawn("BLACK") #Black
                self.__positions__[6][i] = Pawn("WHITE") #White


        #Le damos posiciones a las Reinas negras y blancas#

            self.__positions__[0][3] = Queen("BLACK") #Black
            self.__positions__[7][3] = Queen("WHITE") #White

        #Le damos posiciones a los Reyes negros y blancos#

            self.__positions__[0][4] = Kings("BLACK") #Black
            self.__positions__[7][4] = Kings("WHITE") #White


    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    #Sirve para obtener la pieza
    
    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece): #Coloca las piezas en su posicion
        self.__positions__[row][col] = piece
    
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
    
    #Sirve para obtener los movimientos de las reinas para luego usarlos en el tablero
    def get_Queen_moves(self, row, col):
        queen = self.get_piece(row, col)
        if isinstance(queen, Queen):
            return queen.movimientos_basicos_de_reinas(row, col)
        else:
            return []
        
    #Sirve para obtener los movimientos de los reyes para luego usarlos en el tablero
    def get_Kings_moves(self, row, col):
        kings = self.get_piece(row, col)
        if isinstance(kings, Kings):
            return kings.movimientos_basicos_de_reyes(row, col)
        else:
            return []
        
    def get_Horse_moves(self, row, col):
        horse = self.get_piece(row, col)
        if isinstance(horse, Horse):
            return horse.movimientos_basicos_de_caballos(row, col)
        else:
            return []
    
    def get_pawn_moves(self, row, col):
        pawn = self.get_piece(row, col)
        if isinstance(pawn, Pawn):
            return pawn.movimientos_basicos_de_peones(row, col)
        else:
            return []
        
    #############################

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)