import unittest
from ajedrez.totalpieces.alfils import Alfils


class TestAlfils(unittest.TestCase):

    def setUp(self):
        self.alfils = Alfils("BLACK")
    def test_movimientos_basicos_de_alfiles_negros(self):

        #Sigo el mismo proceso que con los test de Rook, le doy las casillas que deberia usar y 
        #verifico que el resultado sea el esperado

        # Movimientos cruzados de la posición (0, 2) NEGROS
        movimientos_esperados_02 = [(1, 1), (2, 0), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
        self.assertEqual(self.alfils.movimientos_basicos_de_alfiles(0, 2), movimientos_esperados_02)

        # Movimientos cruzados de la posición (0, 5) NEGROS
        movimentos_esperados_05 = [(1, 4), (2, 3), (3, 2), (4, 1), (5, 0), (1, 6), (2, 7)]
        self.assertEqual(self.alfils.movimientos_basicos_de_alfiles(0, 5), movimentos_esperados_05)

    def test_movimientos_basicos_de_alfiles_blancos(self):

        #Movimientos cruzados de la posición (7, 2) BLANCOS
        movimientos_esperados_72 = [(6, 1), (5, 0), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7)]
        self.assertEqual(self.alfils.movimientos_basicos_de_alfiles(7, 2), movimientos_esperados_72)

        #Movimientos cruzados de la posición (7, 5) BLANCOS
        movimentos_esperados_75 = [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0), (6, 6), (5, 7)]
        self.assertEqual(self.alfils.movimientos_basicos_de_alfiles(7, 5), movimentos_esperados_75)
    
    #FUNCIONAAAA

if __name__ == '__main__':
    unittest.main()