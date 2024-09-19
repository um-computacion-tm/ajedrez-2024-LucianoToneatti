from ajedrez.board import Board
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True
    
    def move(self, from_row, from_col, to_row, to_col):
        # Obtener la pieza de la posición de origen desde el tablero
        origin = self.__board__.get_piece(from_row, from_col)

        # Verificar que la pieza existe
        if origin is None:
            raise EmptyPosition("Ninguna pieza en la posición inicial.")
        
        # Verificar que la pieza es del turno actual
        if origin.__color__ != self.__turn__:
            raise InvalidTurn(f"Es el turno de {self.__turn__}")
        
        # Obtener los movimientos válidos de la pieza en la posición actual
        valid_moves = origin.valid_moves(from_row, from_col, self.__board__)

        # Verificar si el movimiento está en los movimientos válidos
        if (to_row, to_col) not in valid_moves:
            raise InvalidMove("Movimiento no válido para la pieza.")

        # Realizar el movimiento si es válido
        self.__board__.set_piece(to_row, to_col, origin)
        self.__board__.set_piece(from_row, from_col, None)

        # Cambiar el turno después de un movimiento exitoso
        self.change_turn()
  
    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"  