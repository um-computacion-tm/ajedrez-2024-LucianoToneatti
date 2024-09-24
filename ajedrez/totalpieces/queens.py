from ajedrez.pieces import Piece
from ajedrez.totalpieces import DIAGONAL_DIRECCIONES
from ajedrez.totalpieces import ORTOGONAL_DIRECCIONES

###REINAS###
class Queen(Piece): #Al parecer a los test no le gustan las herencias multiples entonces tuve que arreglar mi clase Queen

    black_str ="♕"
    white_str ="♛"
    direcciones = ORTOGONAL_DIRECCIONES + DIAGONAL_DIRECCIONES

    def __init__(self, color):
        super().__init__(color)

    # def valid_moves(self, row, col, board): #Usa los movimientos de las torres y los alfiles

    #     moves = self.rook.valid_moves(row, col, board)
    #     moves += self.alfils.valid_moves(row, col, board)
    #     return moves

    def valid_moves(self, row, col, board):
        return self.valid_moves_in_directions(row, col, self.direcciones, board)
#############