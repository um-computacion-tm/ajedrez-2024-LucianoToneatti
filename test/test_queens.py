import unittest
from ajedrez.totalpieces.queens import Queen
from ajedrez.pieces import Piece

class TestQueens(unittest.TestCase):

    def setUp(self):

        self.queen_white = Queen("WHITE")
        self.queen_black = Queen("BLACK")

        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_movimientos_basicos_de_reinas(self):

        self.board[7][3] = self.queen_black
        movimientos_esperados_73 = [(6, 3), (5, 3), (4, 3), (3, 3), (2, 3), 
                                    (1, 3),(0, 3),(7, 2),(7, 1),(7, 0),(7, 4), 
                                    (7, 5), (7, 6), (7, 7),(6, 2), (5, 1), (4, 0),
                                    (6, 4), (5, 5), (4, 6), (3, 7)]
        
        self.assertEqual(self.queen_black.valid_moves(7, 3, self.board), movimientos_esperados_73)

    #Muy dificil de contar todas las posibilidades de movimientos y luego ordenarlas de manera correcta
    # pero funciono!!!!. Ahora aunque no quiera voy a probar un lugar random del tablero.

    def test_movimientos_basicos_de_reinas_con_obstrucciones(self):

        self.board[7][3] = self.queen_white
        self.board[4][3] = Piece ("WHITE")
        self.board[7][5] = Piece ("WHITE")
        self.board[4][0] = Piece ("WHITE")
        self.board[4][6] = Piece ("WHITE")

        movimientos_esperados_73 = [(6, 3), (5, 3), (7, 2), (7, 1), (7, 0), (7, 4), 
                                    (6, 2), (5, 1), (6, 4), (5, 5)]
        self.assertEqual(self.queen_white.valid_moves(7, 3, self.board), movimientos_esperados_73)


    def test_movimientos_basicos_de_reinas_con_captura(self):
        self.board[6][6] = self.queen_black
        self.board[7][7] = Piece ("WHITE")
        self.board[2][2] = Piece ("WHITE")
        self.board[5][7] = Piece ("WHITE")
        self.board[7][5] = Piece ("WHITE")
        self.board[2][6] = Piece ("WHITE")

        movimientos_esperados_66 = [(5, 6), (4, 6), (3, 6), (2, 6), (7, 6), 
                                    (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), 
                                    (6, 0), (6, 7), (5, 5), (4, 4), (3, 3),
                                    (2, 2), (5, 7), (7, 5), (7, 7)]
        self.assertEqual(self.queen_black.valid_moves(6, 6, self.board), movimientos_esperados_66)

    #ME FUNCIONAAAAAA QUE LOCURAAAAA 

if __name__ == '__main__':
    unittest.main()

