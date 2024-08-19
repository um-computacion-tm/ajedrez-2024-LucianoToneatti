class Piece:    #Clase Padre
    def __init__(self, color):
        self.__color__ = color

    @property             #Me toma como objeto privado el color entonces vi que si hago @property lo solucionaba
    
    def color(self):
        return self.__color__

###Tipo de Piezas###

###TORRES###
class Rook(Piece):     
    def __init__(self, color):
        super().__init__(color) 

    def movimientos_basicos_de_torres(self, row, col):

        moves = []

        # Muestra los Movimientos verticales (arriba y abajo) a los que poder mover tu torre
        for r in range(8):
            if r != row:
                moves.append((r, col))

        # Movimientos los horizontales (izquierda y derecha) a los que puede mover tu torre
        for c in range(8):
            if c != col:
                moves.append((row, c))

        return moves
#############

###ALFILS###
class Alfils(Piece):
    
    def __init__(self, color):
        super().__init__(color) 

    def movimientos_basicos_de_alfiles(self, row, col):
        
        moves = []

        #Voy a marcar las "row" como r para mayor comodidad y "col" como c

        ###ARRIBA IZQUIERDA###

        r, c = row -1, col -1 #Les resto 1 para hacer los movimentos arriba izquierda
        while r >=0 and c >=0:#Me permite hacer el movimiento las veces que quiera hasta que me salga del tablero en ese caso se corta el bucle
            moves.append((r, c)) #Los agrego
            r -= 1
            c -= 1

        ###ARRIBA DERECHA###

        r, c = row -1, col +1
        while r >=0 and c <=7:
            moves.append((r, c)) 
            r -= 1
            c += 1

        ###ABAJO IZQUIERDA###

        r, c = row +1, col -1
        while r <=7 and c >=0:
            moves.append((r, c)) 
            r += 1
            c -= 1

        ###ABAJO DERECHA###

        r, c = row +1, col +1
        while r <=7 and c <=7:
            moves.append((r, c)) 
            r += 1
            c += 1

        return moves
    
#############

###REYES###
class Knight(Piece):
    
    def __init__(self, color):
        super().__init__(color)

    def movimientos_basicos_de_reyes(self, row, col):

        moves = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    #Le marque las casillas a las que puede ir y luego direc_row recorre las filas y direc_col las columnas
        for direc_row, direc_col in direcciones:#de esta manera se les va agregar la nueva direccion
            nueva_fila, nueva_columna = row + direc_row, col + direc_col

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:# Verifica que la nueva posición esté dentro del tablero
                moves.append((nueva_fila, nueva_columna))

        return moves


#############

###REINAS###
class Queen(Piece): #Al parecer a los test no le gustan las herencias multiples entonces tuve que arreglar mi clase Queen

    def __init__(self, color):
        super().__init__(color)

        self.rook = Rook(color) 
        self.alfils = Alfils(color)

    def movimientos_basicos_de_reinas(self, row, col): #Usa los movimientos de las torres y los alfiles

        moves = self.rook.movimientos_basicos_de_torres(row, col)
        moves += self.alfils.movimientos_basicos_de_alfiles(row, col)
        return moves

#############

###CABALLOS###
class Horse(Piece):
    pass
#############

###PEONES###
class Pawn(Piece):     
    pass
#############