import unittest
from board import Board
from board import get_piece

class Chess:

    def __init__(self):
        self.__board__ = Board() # 8x8
        self.__turn__ = "WHITE" # white or black

    def move(self,from_row, from_col, to_row, to_col,): # Coordenadas from (x,y) to (x,y)

        #Acordate de validar las coordenadas#

    #########Añade la pieza del tablero###########
        piece = self.board.get_piece(from_row, from_col)
    ###############################################


    #########Cambiar de turno########
        self.change_turn()
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
    ##################################

   

