from ajedrez.pieces import Rook
class Board:

    def __init__(self): # Crear un tablero de 8x8 
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #Le damos posiciones a las torres Black y White#   

        self.__positions__[0][0] = Rook("BLACK") #Black
        self.__positions__[0][7] = Rook("BLACK") #Black
        self.__positions__[7][7] = Rook("WHITE") #White 
        self.__positions__[7][0] = Rook("WHITE") #White

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
        
        #Todavia no implemento la colicion de piezas