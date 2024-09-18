import unittest
from ajedrez.totalpieces.kings import Kings
from ajedrez.pieces import Piece

class TestKings(unittest.TestCase):

    def setUp(self):
        self.king_white = Kings("WHITE")
        self.king_black = Kings("BLACK")

        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_movimientos_basicos_de_reyes(self):
        
        self.board[7][4] = self.king_black

        movimientos_esperados_74 = [(6,3),(6,4),(6,5),(7,3),(7,5)]

        self.assertEqual(self.king_black.valid_moves(7, 4, self.board), movimientos_esperados_74)

    def test_movimientos_basicos_de_reyes_con_colision(self):

        self.board[7][4] = self.king_black
        self.board[6][3] = Piece("BLACK")
        self.board[6][4] = Piece("BLACK")
        self.board[6][5] = Piece("BLACK")
        self.board[7][3] = Piece("BLACK")
        self.board[7][5] = Piece("BLACK")

        movimientos_esperados_74 = []

        self.assertEqual(self.king_black.valid_moves(7, 4, self.board), movimientos_esperados_74)

    def test_movimientos_basicos_de_reyes_con_captura(self):

        self.board[7][4] = self.king_black
        self.board[6][3] = Piece("WHITE")
        self.board[6][4] = Piece("WHITE")
        self.board[6][5] = Piece("WHITE")
        self.board[7][3] = Piece("WHITE")
        self.board[7][5] = Piece("WHITE")

        movimientos_esperados_74 = [(6,3),(6,4),(6,5),(7,3),(7,5)]

        self.assertEqual(self.king_black.valid_moves(7, 4, self.board), movimientos_esperados_74)



if __name__ == '__main__':
    unittest.main()
    

