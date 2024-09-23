from ajedrez.chess import Chess
from ajedrez.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():

    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):

    try:
        print("VAMOS A JUGAR UNA PARTIDA DE AJEDREZ")
        print(chess.show_board())
        print("turn: ", chess.turn)

        from_row = int(input("From row the 0 to 7: "))
        from_col = int(input("From col the 0 to 7: "))
        to_row = int(input("To Row the 0 to 7: "))
        to_col = int(input("To Col the 0 to 7: "))

        chess.move(from_row,from_col,to_row,to_col,)

    except InvalidTurn as e:
        print(e)

    except EmptyPosition as e:
        print(e)

    except InvalidMove as e:
        print(e)

    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    main()
