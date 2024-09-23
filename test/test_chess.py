import unittest
from ajedrez.chess import Chess
from ajedrez.pieces import Piece
from ajedrez.totalpieces.rook import Rook
from ajedrez.totalpieces.pawn import Pawn
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition
from ajedrez.board import Board

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())
    """
    def test_move(self):
        # Creamos un tablero vacío
        board = Board(for_test=True)

        # Colocamos una pawn blanca en la posición (7, 2) del tablero
        board.set_piece(6, 1, Pawn("WHITE"))

        # Establecemos el tablero en el objeto Chess
        setattr(self.chess, '_Chess__board__', board)

        # Movemos la pawn blanca a la posición (5, 2)
        self.chess.move(6, 1, 5, 1)

        # Comprobamos que la pawn blanca está en la posición (5, 2)
        self.assertIsInstance(board.get_piece(5, 1), Pawn)
        self.assertEqual(board.get_piece(5, 1).color, "WHITE")

        # Comprobamos que la posición (7, 2) está vacía
        self.assertIsNone(board.get_piece(6, 1))

        # Comprobamos que el turno ha cambiado
        self.assertEqual(self.chess.turn, "BLACK")
    """
    def test_change_turn(self):
        # Comprobamos que el turno inicial es "WHITE"
        self.assertEqual(self.chess.turn, "WHITE")

        # Cambiamos el turno
        self.chess.change_turn()

        # Comprobamos que el turno ha cambiado a "BLACK"
        self.assertEqual(self.chess.turn, "BLACK")

        # Cambiamos el turno de nuevo
        self.chess.change_turn()

        # Comprobamos que el turno ha vuelto a ser "WHITE"
        self.assertEqual(self.chess.turn, "WHITE")

    def test_move_invalid_turn(self):
        # Creamos un tablero vacío
        board = Board(for_test=True)

        # Colocamos una torre negra en la posición (0, 0) del tablero
        board.set_piece(0, 0, Rook("BLACK"))

        # Establecemos el tablero en el objeto Chess
        setattr(self.chess, '_Chess__board__', board)

        # Intentamos mover la torre negra en el turno de las blancas
        with self.assertRaises(InvalidTurn):
            self.chess.move(0, 0, 1, 0)

    def test_move_invalid_move(self):
        # Creamos un tablero vacío
        board = Board(for_test=True)

        # Colocamos una torre blanca en la posición (7, 0) del tablero
        board.set_piece(7, 0, Rook("WHITE"))

        # Establecemos el tablero en el objeto Chess
        setattr(self.chess, '_Chess__board__', board)

        # Intentamos mover la torre blanca a una posición no válida
        with self.assertRaises(InvalidMove):
            self.chess.move(7, 0, 6, 1)

    def test_move_empty_position(self):
        # Intentamos mover una pieza desde una posición vacía
        with self.assertRaises(EmptyPosition):
            self.chess.move(3, 3, 4, 4)

    
   
if __name__ == '__main__':
    unittest.main()
    