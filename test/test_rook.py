import unittest
from ajedrez.totalpieces.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
            self.rook = Rook("BLACK")#Inicializo la torre de algun color, es indistinto porque se mueven igual

    def test_movimientos_basicos_de_torres(self):

        #Aca lo que haago es decirle antees de correr alguna posición que movimientos son los esperados

        # Movimientos horizontales y verticales de la posición (0, 0)
        movimientos_esperados_00 = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                             (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        self.assertEqual(self.rook.movimientos_basicos_de_torres(0, 0), movimientos_esperados_00)

        # Movimientos horizontales y verticales de la posición (0, 7)
        movimentos_esperados_07 = [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                             (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        self.assertEqual(self.rook.movimientos_basicos_de_torres(0, 7), movimentos_esperados_07)

        # Movimientos horizontales y verticales de la posición (7, 0)
        movimientos_esperados_70 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                             (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        self.assertEqual(self.rook.movimientos_basicos_de_torres(7, 0), movimientos_esperados_70)

        # Movimientos horizontales y verticales de la posición (7, 7)
        movimientos_esperados_77 = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
                             (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]
        self.assertEqual(self.rook.movimientos_basicos_de_torres(7, 7), movimientos_esperados_77)

#Y para comprobar que definitivamente funciona le voy a dar una posicion inicial en (3, 3) 
# para comprobar que funciona de 10

        # Movimientos horizontales y verticales de la posición (3, 3)
        movimientos_esperados_33 = [(0, 3), (1, 3), (2, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                             (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7)]
        self.assertEqual(self.rook.movimientos_basicos_de_torres(3, 3), movimientos_esperados_33)
    
    #FUNCIONAAAAAAAAA

if __name__ == '__main__':
    unittest.main()
