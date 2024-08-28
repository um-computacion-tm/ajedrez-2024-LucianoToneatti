# Changelog
All notable changes to this project will be documented in this file.

# [0.1.5] - 2024-08-28

### Added

-Añadí los test y refactorice mi codigo de Rook para que pueda ademas de moverse capturar y colisionar.

 -Para que funcione mi codigo de Rook y que pueda ademas de moverse colisionar y capturar
    tuve que hacer grandes cambios en mi codigo y dividirlo en 3 funciones principales
    (movimientos basicos, validar colision, validar captura)
    Entonces en vez de hacer que recorra la fila y la columna, separe en 4 secciones 
    izquierda derecha arriba y abajo.

    Primero defino el rango que va a recorrer y cada cuanto y hasta donde.
    Segundo valido colisiones posibles.
    Tercero valido capturas.
    Cuarto devuelve todos los movimientos.

    Aunque al hacer estos cambios y al tener a mi pieza Queen relacionada con los movimientos de la Rook ahora no me andan los Test_Queens, por lo que voy a intentar correguirlo en los siguientes avances.


# [0.1.4] - 2024-08-27

### Added

-Today I added the symbols that the pieces will use in each position they occupy, the symbols are of this style: ♖♕♔♘.


# [0.1.3] - 2024-08-26

### Added

-This time I added what we did with the teacher in class, on the Cli and Chess file, in which we added the movements, the color shifts and soon I will add the Exceptions.

# [0.1.2] - 2024-08-25

### Added

-I added the Pawn Tests and with that I finished testing all the pieces.


# [0.1.1] - 2024-08-24

### Added

-I just finished the Queen's movement tests and they were not difficult, but I did know the correct order of all the squares she can move to.

# [0.1.0] - 2024-08-23

### Added

-I continued with the creation of the Tests, I just made the ones that check the movements of the Horses and the Kings.
-I am in the process of finishing Test_Queen and Test_Pawn

# [0.0.9] - 2024-08-22

### Added

-Today was a challenge, creating the Alfils Tests, but there was an inconvenience when I realized that the Alfils and the Horse were in each other's position. This forced me to edit the Board tests plus change the positions and fix everything so that the game makes sense.

# [0.0.8] - 2024-08-21

### Added

-I created the tests of the Tower's movements and they turned out very well, I did the tests with the 4 corners and also a random position in the middle of the board to see if no problem arose and it worked.

# [0.0.7] - 2024-08-20

### Added

-Create the functions for the movements of the Knight and Pawn. But the function of the pawn's movement when eating pieces is still missing.

# [0.0.6] - 2024-08-19

### Added

-I added the movements of the Kings, I thought it was going to be simpler than the others but there were complications as it was limited to only the nearby squares.
-I also added the function in Board that obtains the movements of the Kings.

# [0.0.5] - 2024-08-18

### Added

-Add queen moves. Reuse of the rook and Alfils functions. That way the code is cleaner and simpler.

# [0.0.4] - 2024-08-17

### Added

-Today's new addition was creating and understanding how the diagonal movement of the Alfils could be done and soon I will use the same code for the queen that moves diagonally.
-Also add the function to obtain the Alfils movements.


# [0.0.3] - 2024-08-16

### Added

-This day was very good because I managed to place the pieces I was missing on the board and classify them by color, in addition to testing it.
-Soon I will try to add the movements to the pieces and I will try to optimize the Test that marks the empty boxes.

# [0.0.2] - 2024-08-15

### Added

-Today I only focused on trying to create a function that allows me to make the movements of the rooks and then send the movements of the rooks to the board.


# [0.0.1] - 2024-08-14

### Added

- In addition to adding everything we saw in class.
- Added tests for the `Board` class that check the initialization of the board, the placement of towers and the correct assignment of the other empty squares.
- And finally configure Dockerfile correctly.
