import unittest
from ajedrez.totalpieces.horse import Horse

class TestHorse(unittest.TestCase):

    def setUp(self):
        
        self.horse = Horse("WHITE")#Inicializo el caballo de algun color y luego le asigno alguna casilla

    def test_movimientos_basicos_de_caballos(self):

        movimientos_esperados_01 = [(1,3), (2,0),(2,2)]

        self.assertEqual(self.horse.movimientos_basicos_de_caballos(0, 1), movimientos_esperados_01)

    #Me di cuenta que con una prueba o algunas puedo saber si el programa funciona o no
    #Entonces no hace falta que pruebe cada caballo en este caso, pero si voy a probar alguna posicion 
    #del tablero aleatoriamente y ver si funciona o no

    def test_movimientos_basicos_de_caballos_aleatorios(self):

        #Movimiento de caballo en (4,4)

        movimientos_esperados_44 = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)]

        self.assertEqual(self.horse.movimientos_basicos_de_caballos(4, 4), movimientos_esperados_44)

    #FUNCIOOOOONAAAAAA

if __name__ == '__main__':
    unittest.main()