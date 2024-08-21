from ajedrez.pieces import Piece

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