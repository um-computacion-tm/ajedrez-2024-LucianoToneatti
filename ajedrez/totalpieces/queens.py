from ajedrez.pieces import Piece
from ajedrez.totalpieces.rook import Rook
from ajedrez.totalpieces.alfils import Alfils

###REINAS###
class Queen(Piece): #Al parecer a los test no le gustan las herencias multiples entonces tuve que arreglar mi clase Queen

    black_str ="♕"
    white_str ="♛"
    

    def __init__(self, color):
        super().__init__(color)

        self.rook = Rook(color) 
        self.alfils = Alfils(color)
        

    def movimientos_basicos_de_reinas(self, row, col, board): #Usa los movimientos de las torres y los alfiles

        moves = self.rook.movimientos_basicos_de_torres(row, col, board)
        moves += self.alfils.movimientos_basicos_de_alfiles(row, col, board)
        return moves

#############