import unittest
from ajedrez.totalpieces.horse import Horse
from ajedrez.pieces import Piece

class TestHorse(unittest.TestCase):

    def setUp(self):
        
        self.horse_white = Horse("WHITE")#Inicializo el caballo de algun color y luego le asigno alguna casilla
        self.horse_black = Horse("BLACK")

        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_movimientos_basicos_de_caballos(self):

        self.board[0][1] = self.horse_white

        movimientos_esperados_01 = [(1,3), (2,0),(2,2)]

        self.assertEqual(self.horse_white.valid_moves(0, 1, self.board), movimientos_esperados_01)

    #Me di cuenta que con una prueba o algunas puedo saber si el programa funciona o no
    #Entonces no hace falta que pruebe cada caballo en este caso, pero si voy a probar alguna posicion 
    #del tablero aleatoriamente y ver si funciona o no

    def test_movimientos_basicos_de_caballos_aleatorios(self):

        self.board[4][4] = self.horse_black

        movimientos_esperados_44 = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)]

        self.assertEqual(self.horse_black.valid_moves(4, 4, self.board), movimientos_esperados_44)

    def test_movimientos_basicos_de_caballos_con_colision(self):

        self.board[4][4] = self.horse_white
        self.board[2][3] = Piece("WHITE")
        self.board[2][5] = Piece("WHITE")
        self.board[3][2] = Piece("WHITE")
        self.board[3][6] = Piece("WHITE")
        self.board[5][2] = Piece("WHITE")
        self.board[5][6] = Piece("WHITE")
        self.board[6][3] = Piece("WHITE")
        self.board[6][5] = Piece("WHITE")

        movimientos_esperados_44 = []

        self.assertEqual(self.horse_white.valid_moves(4, 4, self.board), movimientos_esperados_44)

    def test_movimientos_basicos_de_caballos_con_captura(self):
        self.board[4][4] = self.horse_black
        self.board[2][3] = Piece("WHITE")
        self.assertTrue(self.horse_black.validar_captura(2, 3, self.board))
        self.assertFalse(self.horse_black.validar_captura(3, 2, self.board))


    #FUNCIOOOOONAAAAAA

if __name__ == '__main__':
    unittest.main()