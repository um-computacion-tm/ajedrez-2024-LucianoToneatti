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



        
