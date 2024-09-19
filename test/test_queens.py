import unittest
from ajedrez.totalpieces.queens import Queen
from ajedrez.pieces import Piece
from ajedrez.board import Board

class TestQueens(unittest.TestCase):

    def setUp(self):
        self.queen_white = Queen("WHITE")
        self.queen_black = Queen("BLACK")

        
        self.board = Board(for_test=True)

    def test_movimientos_basicos_de_reinas(self):
        self.board.set_piece(7, 3, self.queen_black)
        
        # Movimientos de la reina desde la posición (7, 3)
        movimientos_esperados_73 = [
            (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), 
            (1, 3), (0, 3), (7, 2), (7, 1), (7, 0), 
            (7, 4), (7, 5), (7, 6), (7, 7), (6, 2), 
            (5, 1), (4, 0), (6, 4), (5, 5), (4, 6), 
            (3, 7)
        ]
        self.assertEqual(self.queen_black.valid_moves(7, 3, self.board), movimientos_esperados_73)

    def test_movimientos_basicos_de_reinas_con_obstrucciones(self):
        self.board.set_piece(7, 3, self.queen_white)
        self.board.set_piece(4, 3, Piece("WHITE"))  
        self.board.set_piece(7, 5, Piece("WHITE"))  
        self.board.set_piece(4, 0, Piece("WHITE"))  
        self.board.set_piece(4, 6, Piece("WHITE"))  

        # Movimientos con obstrucciones desde (7, 3)
        movimientos_esperados_73 = [
            (6, 3), (5, 3), (7, 2), (7, 1), (7, 0), 
            (7, 4), (6, 2), (5, 1), (6, 4), (5, 5)
        ]
        self.assertEqual(self.queen_white.valid_moves(7, 3, self.board), movimientos_esperados_73)

    def test_movimientos_basicos_de_reinas_con_captura(self):
        self.board.set_piece(6, 6, self.queen_black)
        self.board.set_piece(7, 7, Piece("WHITE"))  
        self.board.set_piece(2, 2, Piece("WHITE")) 
        self.board.set_piece(5, 7, Piece("WHITE"))  
        self.board.set_piece(7, 5, Piece("WHITE"))  
        self.board.set_piece(2, 6, Piece("WHITE"))  

        # Movimientos con captura desde (6, 6)
        movimientos_esperados_66 = [
            (5, 6), (4, 6), (3, 6), (2, 6), (7, 6),
            (6, 5), (6, 4), (6, 3), (6, 2), (6, 1),
            (6, 0), (6, 7), (5, 5), (4, 4), (3, 3),
            (2, 2), (5, 7), (7, 5), (7, 7)
        ]
        self.assertEqual(self.queen_black.valid_moves(6, 6, self.board), movimientos_esperados_66)

if __name__ == '__main__':
    unittest.main()


