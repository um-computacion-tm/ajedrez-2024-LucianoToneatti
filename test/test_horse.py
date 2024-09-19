import unittest
from ajedrez.totalpieces.horse import Horse
from ajedrez.pieces import Piece
from ajedrez.board import Board  

class TestHorse(unittest.TestCase):

    def setUp(self):
        self.horse_white = Horse("WHITE")  # Inicializo el caballo de color blanco
        self.horse_black = Horse("BLACK")  # Inicializo el caballo de color negro
        self.board = Board(for_test=True)  # Usamos un tablero adecuado para las pruebas

    def test_movimientos_basicos_de_caballos(self):
        # Posicionamos el caballo blanco en (0, 1)
        self.board.set_piece(0, 1, self.horse_white)

        # Movimientos esperados del caballo en (0, 1)
        movimientos_esperados_01 = [(1, 3), (2, 0), (2, 2)]

        self.assertEqual(self.horse_white.valid_moves(0, 1, self.board), movimientos_esperados_01)

    def test_movimientos_basicos_de_caballos_aleatorios(self):
        # Posicionamos el caballo negro en (4, 4)
        self.board.set_piece(4, 4, self.horse_black)

        # Movimientos esperados del caballo en (4, 4)
        movimientos_esperados_44 = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)]

        self.assertEqual(self.horse_black.valid_moves(4, 4, self.board), movimientos_esperados_44)

    def test_movimientos_basicos_de_caballos_con_colision(self):
        # Posicionamos el caballo blanco en (4, 4) rodeado por piezas blancas
        self.board.set_piece(4, 4, self.horse_white)
        self.board.set_piece(2, 3, Piece("WHITE"))
        self.board.set_piece(2, 5, Piece("WHITE"))
        self.board.set_piece(3, 2, Piece("WHITE"))
        self.board.set_piece(3, 6, Piece("WHITE"))
        self.board.set_piece(5, 2, Piece("WHITE"))
        self.board.set_piece(5, 6, Piece("WHITE"))
        self.board.set_piece(6, 3, Piece("WHITE"))
        self.board.set_piece(6, 5, Piece("WHITE"))

        # El caballo no debería poder moverse ya que está bloqueado por piezas del mismo color
        movimientos_esperados_44 = []

        self.assertEqual(self.horse_white.valid_moves(4, 4, self.board), movimientos_esperados_44)

    def test_movimientos_basicos_de_caballos_con_captura(self):
        # Posicionamos el caballo negro en (4, 4) con una pieza blanca en (2, 3)
        self.board.set_piece(4, 4, self.horse_black)
        self.board.set_piece(2, 3, Piece("WHITE"))

        # Verificamos que el caballo pueda capturar la pieza en (2, 3)
        self.assertTrue(self.horse_black.validar_captura(2, 3, self.board))

        # Verificamos que no puede capturar una pieza en (3, 2) ya que no hay una
        self.assertFalse(self.horse_black.validar_captura(3, 2, self.board))

if __name__ == '__main__':
    unittest.main()
