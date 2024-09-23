import unittest
from ajedrez.totalpieces.pawn import Pawn
from ajedrez.pieces import Piece
from ajedrez.board import Board 

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.pawn_white = Pawn("WHITE")
        self.pawn_black = Pawn("BLACK")
        # Asegúrate de usar el tablero adecuado para las pruebas
        self.board = Board(for_test=True)
        self.primer_movimiento_realizado = False

    def test_movimientos_basicos_de_peones_blancos(self):
        self.board.set_piece(6, 0, self.pawn_white)
        # Movimientos básicos de peones blancos desde (6, 0)
        movimientos_esperados_60 = [(5, 0), (4, 0)]
        self.assertEqual(self.pawn_white.valid_moves(6, 0, self.board), movimientos_esperados_60)

    def test_movimineots_basicos_de_peones_negros(self):
        self.board.set_piece(1, 4, self.pawn_black)

        # Movimiento esperado del peon negro en (1,4)
        movimientos_esperados_14 = [(2, 4), (3, 4)]
        self.assertEqual(self.pawn_black.valid_moves(1, 4, self.board), movimientos_esperados_14)

        # Movimiento esperado del peon negro en un lugar aleatorio en (4,5)
        self.board.set_piece(4, 5, self.pawn_black)
        movimientos_esperados_45 = [(5, 5)]
        self.assertEqual(self.pawn_black.valid_moves(4, 5, self.board), movimientos_esperados_45)

    # Este codigo lo deje para el final mientras pensaba como lo iba hacer, pero me complique la vida 
    # al pedo porque fue como los demas, solo que le tenes que cambiar el color al peon.

    # Lo unico que faltaria seria modificar y hacer que solo en el primer movimiento del peon pueda 
    # moverse dos lugares o uno y apartir de ahi solo un movimiento.
    # Ademas de comer cruzado.

    def test_movimientos_basicos_de_peones_negros_colision(self):
        self.board.set_piece(1, 1, self.pawn_black)
        self.board.set_piece(2, 1, Piece("BLACK"))
        movimientos_esperados_11 = []  # No puede moverse hacia adelante si hay una pieza
        self.assertEqual(self.pawn_black.valid_moves(1, 1, self.board), movimientos_esperados_11)

    def test_movimientos_basicos_de_peones_blancos_colision(self):
        self.board.set_piece(6, 1, self.pawn_white)
        self.board.set_piece(5, 1, Piece("WHITE"))
        movimientos_esperados_61 = []  # No puede moverse hacia adelante si hay una pieza
        self.assertEqual(self.pawn_white.valid_moves(6, 1, self.board), movimientos_esperados_61)

    def test_movimientos_basicos_de_peones_negros_captura(self):
        self.board.set_piece(1, 1, self.pawn_black)
        self.board.set_piece(2, 2, Piece("WHITE"))  # Captura en diagonal derecha
        self.board.set_piece(2, 0, Piece("WHITE"))  # Captura en diagonal izquierda
        movimientos_esperados_11 = [(2, 0), (2, 2), (2, 1), (3, 1)]
        self.assertEqual(self.pawn_black.valid_moves(1, 1, self.board), movimientos_esperados_11)

    def test_movimientos_basicos_de_peones_negros_sin_saltar_piezas_y_capturando(self):
        self.board.set_piece(4, 4, self.pawn_black)
        self.board.set_piece(5, 4, Piece("BLACK"))  # Obstáculo directo enfrente
        self.board.set_piece(5, 5, Piece("WHITE"))  # Pieza enemiga para capturar
        self.board.set_piece(5, 3, Piece("WHITE"))  # Pieza enemiga para capturar
        movimientos_esperados_44 = [(5, 3), (5, 5)]  # Solo puede capturar en diagonal
        self.assertEqual(self.pawn_black.valid_moves(4, 4, self.board), movimientos_esperados_44)

if __name__ == '__main__':
    unittest.main()

