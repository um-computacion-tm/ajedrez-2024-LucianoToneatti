from ajedrez.pieces import Piece

###PEONES###
class Pawn(Piece):     
    
    def __init__(self, color):
        super().__init__(color)

    def movimientos_basicos_de_peones(self, row, col):

        moves = []

        if self.__color__ == "BLACK": #Primero pregunto el color de la pieza 

            direcciones = [(1, 0), (2, 0)] #Le asigno sus posibles movimientos segun el color
        
        elif self.__color__ == "WHITE":

            direcciones = [(-1, 0), (-2, 0)]
        
        for direc_row, direc_col in direcciones: #Despues recorro la lista de direcciones segun lo que alla tocado

            nueva_fila, nueva_columna = row + direc_row, col + direc_col #Le asigno la nueva posision 
                
            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8: #Y aca compruebo q no se salga el tablero
                moves.append((nueva_fila, nueva_columna))

        #En pocas palabras este codigo es diferente a los demas porque es una pieza la cual 
        # sus movimientos dependen de su color, y luego añadire los movimientos de cuando 
        # come otra pieza

        return moves
            
#############