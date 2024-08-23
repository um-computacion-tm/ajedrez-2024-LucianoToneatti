import unittest
from ajedrez.totalpieces.kings import Kings

class TestKings(unittest.TestCase):

    def setUp(self):
        self.king = Kings("WHITE")

    def test_movimientos_basicos_de_reyes(self):
        
        movimientos_esperados_74 = [(6,3),(6,4),(6,5),(7,3),(7,5)]

        self.assertEqual(self.king.movimientos_basicos_de_reyes(7, 4), movimientos_esperados_74)

if __name__ == '__main__':
    unittest.main()
    

