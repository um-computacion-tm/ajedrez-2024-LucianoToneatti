from ajedrez.pieces import Piece
from ajedrez.totalpieces import ORTOGONAL_DIRECCIONES

###TORRES###
class Rook(Piece):     

    black_str ="♖"
    white_str ="♜"
    direcciones = ORTOGONAL_DIRECCIONES
    
    def __init__(self, color):
        super().__init__(color) 

    def valid_moves(self, row, col, board):
        return self.valid_moves_in_directions(row, col, self.direcciones, board)

    ########################

        #Para que funcione mi codigo de Rook y que pueda ademas de moverse colisionar y capturar
        #   tuve que hacer grandes cambios en mi codigo y dividirlo en 3 funciones principales
        #   (movimientos basicos, validar colision, validar captura)
        #Entonces en vez de hacer que recorra la fila y la columna, separe en 4 secciones 
        #   izquierda derecha arriba y abajo

        #Primero defino el rango que va a recorrer y cada cuanto y hasta donde
        #Segundo valido colisiones posibles
        #Tercero valido capturas
        #Cuarto devuelve todos los movimientos



        
