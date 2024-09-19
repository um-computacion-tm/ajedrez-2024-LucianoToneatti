from ajedrez.pieces import Piece


###TORRES###
class Rook(Piece):     

    black_str ="♖"
    white_str ="♜"
    
    def __init__(self, color):
        super().__init__(color) 

    def validar_colision(self, row, col, board):
        #Verifica si hay colisión con una pieza del mismo color en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ == self.__color__

    def validar_captura(self, row, col, board):
        #Verifica si la torre puede capturar una pieza enemiga en la posición dada
        pieza = board.get_piece(row, col)
        return pieza is not None and pieza.__color__ != self.__color__

    def valid_moves(self, row, col, board):

        moves = []

        # Muestra movimientos hacia arriba
        for r in range(row - 1, -1, -1):
            if self.validar_colision(r, col, board):
                break
            if self.validar_captura(r, col, board):
                moves.append((r, col))
                break
            moves.append((r, col))

        # Muestra movimientos hacia abajo
        for r in range(row + 1, 8):
            if self.validar_colision(r, col, board):
                break
            if self.validar_captura(r, col, board):
                moves.append((r, col))
                break
            moves.append((r, col))

        # MuestraMovimiento hacia la izquierda
        for c in range(col - 1, -1, -1):
            if self.validar_colision(row, c, board):
                break
            if self.validar_captura(row, c, board):
                moves.append((row, c))
                break
            moves.append((row, c))

        # Muestra Movimiento hacia la derecha
        for c in range(col + 1, 8):
            if self.validar_colision(row, c, board):
                break
            if self.validar_captura(row, c, board):
                moves.append((row, c))
                break
            moves.append((row, c))

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



        
