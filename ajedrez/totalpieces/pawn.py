from ajedrez.pieces import Piece

###PEONES###
class Pawn(Piece):

    black_str = "♙"
    white_str = "♟"

    def __init__(self, color):
        super().__init__(color)
        self.primer_movimiento_realizado = False

    def obtener_direcciones(self):
        if self.__color__ == "BLACK":
            if not self.primer_movimiento_realizado:
                return [(1, 0), (2, 0)]
            else:
                return [(1, 0)]
        elif self.__color__ == "WHITE":
            if not self.primer_movimiento_realizado:
                return [(-1, 0), (-2, 0)]
            else:
                return [(-1, 0)]

    def es_movimiento_valido(self, row, col, direc_row, direc_col, board):
        # Verifica si un movimiento es válido según reglas del peón.
        new_row, new_col = row + direc_row, col + direc_col
        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            return False
        if self.validar_colision(new_row, new_col, board):
            return False
        if abs(direc_row) == 2:
            fila_intermedia = row + direc_row // 2
            if board.get_piece(fila_intermedia, col) is not None:
                return False
        return True

    def valid_moves(self, row, col, board):
        # Obtiene movimientos básicos del peón según posición y tablero.
        moves = []

        # Capturas en diagonales #
        direcciones_captura = [(1, -1), (1, 1)] if self.__color__ == "BLACK" else [(-1, -1), (-1, 1)]
        for direc_row, direc_col in direcciones_captura:
            new_row, new_col = row + direc_row, col + direc_col
            if 0 <= new_row < 8 and 0 <= new_col < 8 and self.validar_captura(new_row, new_col, board):
                moves.append((new_row, new_col))

        # Movimientos hacia adelante #
        direcciones = self.obtener_direcciones()
        for direc_row, direc_col in direcciones:
            if self.es_movimiento_valido(row, col, direc_row, direc_col, board):
                moves.append((row + direc_row, col + direc_col))

        if not self.primer_movimiento_realizado:
            self.primer_movimiento_realizado = True
        return moves

    
    #########################