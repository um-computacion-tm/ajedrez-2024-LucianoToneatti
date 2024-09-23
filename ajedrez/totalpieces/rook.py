from ajedrez.pieces import Piece


###TORRES###
class Rook(Piece):     

    black_str ="♖"
    white_str ="♜"
    
    def __init__(self, color):
        super().__init__(color) 

    def valid_moves(self, row, col, board):
        moves = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direc_row, direc_col in direcciones:
            moves.extend(self.valid_moves_in_direction(row, col, direc_row, direc_col, board))
        return moves

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



        
