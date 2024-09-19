import unittest
from ajedrez.totalpieces.alfils import Alfils
from ajedrez.pieces import Piece
from ajedrez.board import Board

class TestAlfils(unittest.TestCase):

    def setUp(self):
        self.alfils_black = Alfils("BLACK")
        self.alfils_white = Alfils("WHITE")

        self.board = Board(for_test=True)  

    def test_movimientos_basicos_de_alfiles(self):
        self.board.set_piece(0, 2, self.alfils_black)
        
        # Movimientos cruzados de la posición (0, 2) para la pieza negra
        movimientos_esperados_02 = [(1, 1), (2, 0), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
        self.assertEqual(self.alfils_black.valid_moves(0, 2, self.board), movimientos_esperados_02)

    def test_movimientos_basicos_de_alfiles_con_obstrucciones(self):
        self.board.set_piece(4, 4, self.alfils_black)
        self.board.set_piece(2, 2, Piece("BLACK"))
        self.board.set_piece(5, 3, Piece("BLACK"))
        self.board.set_piece(7, 7, Piece("BLACK"))

        # Movimientos cruzados de la posición (4, 4) para la pieza negra con obstrucciones
        movimientos_esperados_44 = [(3, 3), (3, 5),(2, 6), (1, 7), (5, 5), (6, 6)]
        self.assertEqual(self.alfils_black.valid_moves(4, 4, self.board), movimientos_esperados_44)

    def test_movimientos_basicos_de_alfiles_con_captura(self):
        self.board.set_piece(4, 4, self.alfils_black)
        self.board.set_piece(2, 2, Piece("WHITE"))
        self.board.set_piece(5, 3, Piece("WHITE"))
        self.board.set_piece(7, 7, Piece("WHITE"))
        self.board.set_piece(1, 7, Piece("WHITE"))

        # Movimientos cruzados de la posición (4, 4) para la pieza negra con captura
        movimientos_esperados_44 = [(3, 3), (2, 2), (3, 5), (2, 6), (1, 7), (5, 3), (5, 5), (6, 6), (7, 7)]
        self.assertEqual(self.alfils_black.valid_moves(4, 4, self.board), movimientos_esperados_44)

if __name__ == '__main__':
    unittest.main()
