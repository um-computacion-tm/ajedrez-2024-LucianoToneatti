import unittest
from ajedrez.totalpieces.kings import Kings
from ajedrez.pieces import Piece
from ajedrez.board import Board 

class TestKings(unittest.TestCase):

    def setUp(self):
        self.king_white = Kings("WHITE")
        self.king_black = Kings("BLACK")
       
        self.board = Board(for_test=True)

    def test_movimientos_basicos_de_reyes(self):
        # Posicionamos el rey negro en (7, 4)
        self.board.set_piece(7, 4, self.king_black)

        # Movimientos esperados del rey en (7, 4)
        movimientos_esperados_74 = [(6, 3), (6, 4), (6, 5), (7, 3), (7, 5)]

        self.assertEqual(self.king_black.valid_moves(7, 4, self.board), movimientos_esperados_74)

    def test_movimientos_basicos_de_reyes_con_colision(self):
        # Posicionamos el rey negro en (7, 4) rodeado por piezas del mismo color
        self.board.set_piece(7, 4, self.king_black)
        self.board.set_piece(6, 3, Piece("BLACK"))
        self.board.set_piece(6, 4, Piece("BLACK"))
        self.board.set_piece(6, 5, Piece("BLACK"))
        self.board.set_piece(7, 3, Piece("BLACK"))
        self.board.set_piece(7, 5, Piece("BLACK"))

        # Rey no debería poder moverse a ninguna casilla porque está bloqueado
        movimientos_esperados_74 = []

        self.assertEqual(self.king_black.valid_moves(7, 4, self.board), movimientos_esperados_74)

    def test_movimientos_basicos_de_reyes_con_captura(self):
        # Posicionamos el rey negro en (7, 4) con piezas enemigas alrededor
        self.board.set_piece(7, 4, self.king_black)
        self.board.set_piece(6, 3, Piece("WHITE"))
        self.board.set_piece(6, 4, Piece("WHITE"))
        self.board.set_piece(6, 5, Piece("WHITE"))
        self.board.set_piece(7, 3, Piece("WHITE"))
        self.board.set_piece(7, 5, Piece("WHITE"))

        # Rey debería poder moverse a cualquier casilla ocupada por piezas blancas (captura)
        movimientos_esperados_74 = [(6, 3), (6, 4), (6, 5), (7, 3), (7, 5)]

        self.assertEqual(self.king_black.valid_moves(7, 4, self.board), movimientos_esperados_74)

if __name__ == '__main__':
    unittest.main()

    

