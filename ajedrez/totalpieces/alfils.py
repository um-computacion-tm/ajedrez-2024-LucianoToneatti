from ajedrez.pieces import Piece

###ALFILS###
class Alfils(Piece):

    black_str ="♗"
    white_str ="♝"
    
    
    def __init__(self, color):
        super().__init__(color) 

    def validar_colision(self, row, col, board):
        #Verifica si hay colisión con una pieza del mismo color en la posición dada
        pieza = board[row][col]
        return pieza is not None and pieza.__color__ == self.__color__

    def validar_captura(self, row, col, board):
        #Verifica si la torre puede capturar una pieza enemiga en la posición dada
        pieza = board[row][col]
        return pieza is not None and pieza.__color__ != self.__color__


    def movimientos_basicos_de_alfiles(self, row, col, board):
        
        moves = []

        #Voy a marcar las "row" como r para mayor comodidad y "col" como c

        ###ARRIBA IZQUIERDA###

        r, c = row -1, col -1 #Les resto 1 para hacer los movimentos arriba izquierda
        while r >=0 and c >=0:#Me permite hacer el movimiento las veces que quiera hasta que me salga del tablero en ese caso se corta el bucle
            if self.validar_colision(r, c, board):
                break
            if self.validar_captura(r, c, board):
                moves.append((r, c)) #Los agrego
                break
            moves.append((r, c)) #Los agrego
            r -= 1
            c -= 1

        ###ARRIBA DERECHA###

        r, c = row -1, col +1
        while r >=0 and c <=7:
            if self.validar_colision(r, c, board):
                break
            if self.validar_captura(r, c, board):
                moves.append((r, c)) 
                break
            moves.append((r, c)) 
            r -= 1
            c += 1

        ###ABAJO IZQUIERDA###

        r, c = row +1, col -1
        while r <=7 and c >=0:
            if self.validar_colision(r, c, board):
                break
            if self.validar_captura(r, c, board):
                moves.append((r, c)) 
                break
            moves.append((r, c)) 
            r += 1
            c -= 1

        ###ABAJO DERECHA###

        r, c = row +1, col +1
        while r <=7 and c <=7:
            if self.validar_colision(r, c, board):
                break
            if self.validar_captura(r, c, board):
                moves.append((r, c)) 
                break
            moves.append((r, c)) 
            r += 1
            c += 1

        return moves
    
#############