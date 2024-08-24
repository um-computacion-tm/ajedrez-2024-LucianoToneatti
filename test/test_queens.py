import unittest
from ajedrez.totalpieces.queens import Queen


class TestQueens(unittest.TestCase):

    def setUp(self):

        self.queen = Queen("WHITE")

    def test_movimientos_basicos_de_reinas(self):

        movimientos_esperados_73 = [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,0),(7,1),(7,2),
                                    (7,4),(7,5),(7,6),(7,7),(6,2),(5,1),(4,0),(6,4),(5,5),(4,6),(3,7)]
        
        self.assertEqual(self.queen.movimientos_basicos_de_reinas(7, 3), movimientos_esperados_73)

    #Muy dificil de contar todas las posibilidades de movimientos y luego ordenarlas de manera correcta
    # pero funciono!!!!. Ahora aunque no quiera voy a probar un lugar random del tablero.


        movimientos_esperados_32 = [(0, 2), (1, 2), (2, 2), (4, 2), (5, 2), (6, 2), 
                                    (7, 2), (3, 0), (3, 1), (3, 3), (3, 4), (3, 5), 
                                    (3, 6), (3, 7), (2, 1), (1, 0), (2, 3), (1, 4), 
                                    (0, 5), (4, 1), (5, 0), (4, 3), (5, 4), (6, 5), (7, 6)]
        self.assertEqual(self.queen.movimientos_basicos_de_reinas(3, 2), movimientos_esperados_32)

    #ME FUNCIONAAAAAA QUE LOCURAAAAA 

if __name__ == '__main__':
    unittest.main()