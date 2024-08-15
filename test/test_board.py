import unittest
from ajedrez.board import Board
from ajedrez.pieces import Rook
###Test_de_board###

class TestBoard(unittest.TestCase):
    def test_board(self):

        board = Board()

        self.assertEqual(len(board.__positions__), 8) #El tablero  tendra 8 filas??
        for row in board.__positions__: #hace un bucle para cada una de las filas
            self.assertEqual(len(row), 8) #cada una de las filas tiene 8 columnas?

    ### COMPRUEBA EL COLOR DE LAS TORRES Y SU POSICIÓN ###

    ###TORRES NEGRAS###

        self.assertIsInstance(board.__positions__[0][0], Rook, "Debe haber una torre en (0,0)")
        self.assertEqual(board.__positions__[0][0].color, "BLACK", "La torre en (0,0) debe ser negra")
        self.assertIsInstance(board.__positions__[0][7], Rook, "Debe haber una torre en (0,7)")
        self.assertEqual(board.__positions__[0][7].color, "BLACK", "La torre en (0,7) debe ser negra")

    ###TORRES BLANCAS###
        self.assertIsInstance(board.__positions__[7][0], Rook, "Debe haber una torre en (7,0)")
        self.assertEqual(board.__positions__[7][0].color, "WHITE", "La torre en (7,0) debe ser blanca")
        self.assertIsInstance(board.__positions__[7][7], Rook, "Debe haber una torre en (7,7)")
        self.assertEqual(board.__positions__[7][7].color, "WHITE", "La torre en (7,7) debe ser blanca")

    ### COMPRUEBA QUE LAS CASILLAS VACIAS NO TENGAN PIEZAS ###
        for i in range(8):
                    for j in range(8):
                        if (i, j) not in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                            self.assertIsNone(board.get_piece(i, j), f"La posicion ({i},{j}) debe estar vacia")

if __name__ == '__main__':
    unittest.main()
