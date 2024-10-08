import unittest
from ajedrez.board import Board
from ajedrez.totalpieces.rook import Rook
from ajedrez.totalpieces.pawn import Pawn
from ajedrez.totalpieces.queens import Queen
from ajedrez.totalpieces.kings import Kings
from ajedrez.totalpieces.horse import Horse
from ajedrez.totalpieces.alfils import Alfils

from ajedrez.exceptions import OutOfBoard

###Test_de_board###

class TestBoard(unittest.TestCase):
    def test_board(self):

        board = Board()

        self.assertEqual(len(board.__positions__), 8) #El tablero  tendra 8 filas??
        for row in board.__positions__: #hace un bucle para cada una de las filas
            self.assertEqual(len(row), 8) #cada una de las filas tiene 8 columnas?

    ### COMPRUEBA EL COLOR Y SU POSICIÓN ###

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

    ###CABALLOS NEGROS###

        self.assertIsInstance(board.__positions__[0][1], Horse, "Debe haber un caballo en (0,1)")
        self.assertEqual(board.__positions__[0][1].color, "BLACK", "El caballo en (0,1) debe ser negro")
        self.assertIsInstance(board.__positions__[0][6], Horse, "Debe haber un caballo en (0,6)")
        self.assertEqual(board.__positions__[0][6].color, "BLACK", "El caballo en (0,6) debe ser negro")

    ###CABALLOS BLANCOS###

        self.assertIsInstance(board.__positions__[7][1], Horse, "Debe haber un caballo en (7,1)")
        self.assertEqual(board.__positions__[7][1].color, "WHITE", "El caballo en (7,1) debe ser blanco")
        self.assertIsInstance(board.__positions__[7][6], Horse, "Debe haber un caballo en (7,6)")
        self.assertEqual(board.__positions__[7][6].color, "WHITE", "El caballo en (7,6) debe ser blanco")

    ###ALFILES NEGROS###

        self.assertIsInstance(board.__positions__[0][2], Alfils, "Debe haber un alfil en (0,2)")
        self.assertEqual(board.__positions__[0][2].color, "BLACK", "El alfil en (0,2) debe ser negro")
        self.assertIsInstance(board.__positions__[0][5], Alfils, "Debe haber un alfil en (0,5)")
        self.assertEqual(board.__positions__[0][5].color, "BLACK", "El alfil en (0,5) debe ser negro")

    ###ALFILES BLANCOS###                 

        self.assertIsInstance(board.__positions__[7][2], Alfils, "Debe haber un alfil en (7,2)")
        self.assertEqual(board.__positions__[7][2].color, "WHITE", "El alfil en (7,2) debe ser blanco")
        self.assertIsInstance(board.__positions__[7][5], Alfils, "Debe haber un alfil en (7,5)")
        self.assertEqual(board.__positions__[7][5].color, "WHITE", "El alfil en (7,5) debe ser blanco")

    ###REINAS NEGRAS###

        self.assertIsInstance(board.__positions__[0][3], Queen, "Debe haber una reina en (0,3)")
        self.assertEqual(board.__positions__[0][3].color, "BLACK", "La reina en (0,3) debe ser negra")

    ###REINAS BLANCAS###

        self.assertIsInstance(board.__positions__[7][3], Queen, "Debe haber una reina en (7,3)")
        self.assertEqual(board.__positions__[7][3].color, "WHITE", "La reina en (7,3) debe ser negra")

    ###REY NEGRO###

        self.assertIsInstance(board.__positions__[0][4], Kings, "Debe haber un rey en (0,4)")
        self.assertEqual(board.__positions__[0][4].color, "BLACK", "El rey en (0,4) debe ser negro")

    ###REY BLANCO###

        self.assertIsInstance(board.__positions__[7][4], Kings, "Debe haber un rey en (7,4)")
        self.assertEqual(board.__positions__[7][4].color, "WHITE", "El rey en (7,4) debe ser blanco")

    ###PEONES NEGROS###
        for i in range(8):
            self.assertIsInstance(board.__positions__[1][i], Pawn, "Debe haber un peón en (1,i)")
            self.assertEqual(board.__positions__[1][i].color, "BLACK", "El peón en (1,i) debe ser negro")

    ###PEONES BLANCOS###
        for i in range(8):
            self.assertIsInstance(board.__positions__[6][i], Pawn, "Debe haber un peón en (6,i)")
            self.assertEqual(board.__positions__[6][i].color, "WHITE", "El peón en (6,i) debe ser 白")


    ### COMPRUEBA QUE LAS CASILLAS VACIAS NO TENGAN PIEZAS Y TODOS ESTE EN SU LUGAR ###
        for i in range(8):
                    for j in range(8):
                        if (i, j) not in [(0, 0), (0, 7), (7, 0), (7, 7), (0, 1), (0, 6), (7, 1), (7, 6), (0, 2), (0, 5), (7, 2), (7, 5), (0, 3), (0, 4), (7, 3), (7, 4), (1, 0), (1, 7), (6, 0), (6, 7), (1, 1), (1, 6), (6, 1), (6, 6), (1, 2), (1, 5), (6, 2), (6, 5), (1, 3), (1, 4), (6, 3), (6, 4)]:
                            self.assertIsNone(board.get_piece(i, j), f"La posicion ({i},{j}) debe estar vacia")
    ### Debe haber una mejor manera de comprobar que las casillas estan bacias pero a mi solo se me ocurrio 
    ### poner todas las casillas iniciales y que esten ocupadas por alguna ficha.


    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♛♚♝♞♜\n"
            )
        )

    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK')
        board.set_piece(0, 0, rook)

        board.move(
            from_row=0,
            from_col=0,
            to_row=0,
            to_col=1,
        )

        self.assertIsInstance(
            board.get_piece(0, 1),
            Rook,
        )
        self.assertEqual(
            str(board),
            (
                " ♖      \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
            )
        )

    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )


    def test_remove_piece(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK')
        board.set_piece(0, 0, rook)

        board.remove_piece(0, 0)

        self.assertIsNone(board.get_piece(0, 0))

    def test_get_valid_moves(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK')
        board.set_piece(3, 3, rook)

        valid_moves = board.get_valid_moves(3, 3)

        expected_moves = [(3, i) for i in range(8) if i != 3] + [(i, 3) for i in range(8) if i != 3]
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))

    def test_get_valid_moves_empty_position(self):
        board = Board(for_test=True)

        valid_moves = board.get_valid_moves(3, 3)

        self.assertEqual(valid_moves, [])



if __name__ == '__main__':
    unittest.main()
