import unittest
from ajedrez.totalpieces.rook import Rook
from ajedrez.pieces import Piece

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook_black = Rook("BLACK")#Inicializo la torre de algun color, es indistinto porque se mueven igual
        self.rook_white = Rook("WHITE")

        # Creación de un tablero vacío para las pruebas
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_movimientos_basicos_de_torres_sin_obstrucciones(self):

        #Aca lo que haago es decirle antees de correr alguna posición que movimientos son los esperados
        self.board[0][0] = self.rook_black
        # Movimientos horizontales y verticales de la posición (0, 0)
        movimientos_esperados_11 = [(0, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
                                    (6, 1), (7, 1), (1, 0), (1, 2), (1, 3),
                                    (1, 4), (1, 5), (1, 6), (1, 7)]
        self.assertEqual(self.rook_black.valid_moves(1, 1, self.board), movimientos_esperados_11)
    
    def test_movimientos_basicos_de_torres_con_obstrucciones(self):
        # Colocamos la torre en la posición (3, 3) y una pieza compañera en (3, 5)
        self.board[3][3] = self.rook_black
        self.board[3][5] = Piece("BLACK")  # Aliado en el camino
        self.board[1][3] = Piece("BLACK")
        self.board[3][1] = Piece("BLACK")
        self.board[5][3] = Piece("BLACK")


        movimientos_esperados_33 = [(2, 3), (4, 3), (3, 2), (3, 4)]
        self.assertEqual(self.rook_black.valid_moves(3, 3, self.board), movimientos_esperados_33)

    def test_movimientos_basicos_de_torres_con_captura(self):
        # Colocamos la torre en la posición (3, 3) y un enemigo en (3, 5)
        self.board[3][3] = self.rook_black
        self.board[3][5] = Piece("WHITE")  # Enemigo en el camino
        self.board[1][3] = Piece("WHITE")
        self.board[3][1] = Piece("WHITE")
        self.board[5][3] = Piece("WHITE")

        movimientos_esperados_33 = [(2, 3), (1, 3), (4, 3), (5, 3), (3, 2), (3, 1), (3, 4), (3, 5)]  # Se captura en (3, 5)
        self.assertEqual(self.rook_black.valid_moves(3, 3, self.board), movimientos_esperados_33)

    def test_captura_y_colision(self):

        # Colocamos la torre en la ubicación (5, 2) y dos piezas en las ubicaciones (1, 2) y (5, 5)
        self.board[5][2] = self.rook_white
        self.board[1][2] = Piece("WHITE")
        self.board[5][5] = Piece("BLACK")
        self.board[6][2] = Piece("BLACK")

        movimientos_esperados_52 = [(4, 2), (3, 2), (2, 2), (6, 2),
                                    (5, 1), (5, 0), (5, 3), (5, 4),(5, 5)]
        self.assertEqual(self.rook_white.valid_moves(5, 2, self.board), movimientos_esperados_52)



if __name__ == '__main__':
    unittest.main()
