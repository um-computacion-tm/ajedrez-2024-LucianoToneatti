import unittest
from ajedrez.totalpieces.rook import Rook
from ajedrez.totalpieces.pawn import Pawn 
from ajedrez.pieces import Piece
from ajedrez.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook_black = Rook("BLACK")  # Inicializo la torre de algún color, es indistinto porque se mueven igual
        self.rook_white = Rook("WHITE")
        
       
        self.board = Board(for_test=True)

    def test_movimientos_basicos_de_torres_sin_obstrucciones(self):
        self.board.set_piece(0, 0, self.rook_black)
        
        # Movimientos horizontales y verticales de la posición (0, 0)
        movimientos_esperados_00 = [(1, 0), (2, 0), (3, 0),
                                    (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), 
                                    (0, 6), (0, 7)]
        self.assertEqual(self.rook_black.valid_moves(0, 0, self.board), movimientos_esperados_00)

    def test_movimientos_basicos_de_torres_con_obstrucciones(self):
        # Colocamos la torre en la posición (3, 3) y una pieza compañera en (3, 5)
        self.board.set_piece(3, 3, self.rook_black)
        self.board.set_piece(3, 5, Pawn("BLACK"))  # Aliado en el camino
        self.board.set_piece(1, 3, Pawn("BLACK"))
        self.board.set_piece(3, 1, Pawn("BLACK"))
        self.board.set_piece(5, 3, Pawn("BLACK"))

        movimientos_esperados_33 = [(2, 3), (4, 3), (3, 2), (3, 4)]
        self.assertEqual(self.rook_black.valid_moves(3, 3, self.board), movimientos_esperados_33)

    def test_movimientos_basicos_de_torres_con_captura(self):
        # Colocamos la torre en la posición (3, 3) y un enemigo en (3, 5)
        self.board.set_piece(3, 3, self.rook_black)
        self.board.set_piece(3, 5, Pawn("WHITE"))  # Enemigo en el camino
        self.board.set_piece(1, 3, Pawn("WHITE"))
        self.board.set_piece(3, 1, Pawn("WHITE"))
        self.board.set_piece(5, 3, Pawn("WHITE"))

        movimientos_esperados_33 = [(2, 3), (1, 3), (4, 3), (5, 3), (3, 2), (3, 1), (3, 4), (3, 5)]  # Se captura en (3, 5)
        self.assertEqual(self.rook_black.valid_moves(3, 3, self.board), movimientos_esperados_33)

    def test_captura_y_colision(self):
        # Colocamos la torre en la ubicación (5, 2) y dos piezas en las ubicaciones (1, 2) y (5, 5)
        self.board.set_piece(5, 2, self.rook_white)
        self.board.set_piece(1, 2, Pawn("WHITE"))
        self.board.set_piece(5, 5, Pawn("BLACK"))
        self.board.set_piece(6, 2, Pawn("BLACK"))

        movimientos_esperados_52 = [(4, 2), (3, 2), (2, 2), (6, 2),
                                    (5, 1), (5, 0), (5, 3), (5, 4), (5, 5)]
        self.assertEqual(self.rook_white.valid_moves(5, 2, self.board), movimientos_esperados_52)

if __name__ == '__main__':
    unittest.main()

