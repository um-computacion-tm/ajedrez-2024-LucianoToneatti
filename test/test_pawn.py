import unittest
from ajedrez.totalpieces.pawn import Pawn

class TestPawn(unittest.TestCase):


    def setUp(self):
        self.pawn = Pawn("WHITE")


    def test_movimientos_basicos_de_peones_blancos(self):

        movimientos_esperados_60 = [(5,0),(4,0)]

        self.assertEqual(self.pawn.movimientos_basicos_de_peones(6,0), movimientos_esperados_60)

    def test_movimineots_basicos_de_peones_negros(self):

        self.pawn = Pawn("BLACK")

        #Movimiento esperado del peon negro en (1,4)
        movimientos_esperados_14 = [(2,4),(3,4)]

        self.assertEqual(self.pawn.movimientos_basicos_de_peones(1,4), movimientos_esperados_14)

        #Movimiento esperado del peon negro en  un lugar aleatorio en(4,5)
        movimientos_esperados_45 = [(5,5),(6,5)]

        self.assertEqual(self.pawn.movimientos_basicos_de_peones(4,5), movimientos_esperados_45)

    #Este codigo lo deje para el final mientras pensaba como lo iba hacer, pero me complique la vida 
    #   al pedo porque fue como los demas, solo que le tenes que cambiar el color al peon.

    #Lo unico que faltaria seria modificar y hacer que solo en el primer movimiento del peon pueda 
    #   moverse dos lugares o uno y apartir de ahi solo un movimiento.
    #Ademas de comer cruzado.



if __name__ == '__main__':
    unittest.main()