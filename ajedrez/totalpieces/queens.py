from ajedrez.pieces import Piece
from ajedrez.totalpieces import DIAGONAL_DIRECCIONES
from ajedrez.totalpieces import ORTOGONAL_DIRECCIONES

###REINAS###
class Queen(Piece): #Al parecer a los test no le gustan las herencias multiples entonces tuve que arreglar mi clase Queen

    black_str ="♕"
    white_str ="♛"
    direcciones = ORTOGONAL_DIRECCIONES + DIAGONAL_DIRECCIONES
