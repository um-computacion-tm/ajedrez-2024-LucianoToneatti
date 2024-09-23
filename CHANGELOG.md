# Changelog
All notable changes to this project will be documented in this file.

# [0.3.4] - 2024-09-23

### Added

-I started refactoring the validate_capture and validate_collision functions. Delete the functions of all pieces except the validate_collision of "Pawn" and place them in the "Piece" class so that they directly inherit the functions.

-Refactored the "valid_moves" function of "alfils.py" and "rook.py" because they were very complex and in this way they are more readable and cleaner.

# [0.3.3] - 2024-09-22

### Added

-Create the tests for Chess.py

# [0.3.2] - 2024-09-21

### Added

-Added the complete Board tests

# [0.3.1] - 2024-09-19

### Added

-After many errors and investigating why it was the error that would not let me play, I realized that it was because: 

Instead of doing this (which caused me the error): board[row][col]

I had to write it like this: board.get_piece(row, col)

And this was because I was trying to access the object in the wrong way, in short I had to use get_piece to obtain the piece.

-This small change in all the pieces caused all my tests to stop working, not because they were wrong, but it was because of the syntax of how they were written, so I corrected them and now they work completely.

-And finally, I modified the chess moves function so that it worked correctly.


# [0.3.0] - 2024-09-18

### Added

-I wanted to test the game to see how it went and if the exceptions worked but in order to get the game running I had to remove the cli.py from the folder. I also added more tests to the "Board" to check that it would work correctly. Anyway, I'm having an error when I want to move the pieces and I'm trying to solve it.

# [0.2.9] - 2024-09-17

### Added

-I made several changes to my code to make it shorter and more understandable, I changed all the names of the basic_moves_rook basic_moves_alfil etc functions to valid_moves, this way I was able to refactor the get of each piece in Board and only creating one called get_valid_moves.
-When changing the names of the basic movements I also had to correct the name in the tests of each piece.

# [0.2.8] - 2024-09-16

### Added

-Added the exceptions to the cli and added the get for "Horse" and "Pawn". And a str that returns the board to you in the form of a chain and adds the exception to the get piece for when a piece wants to leave the board.

# [0.2.7] - 2024-09-15

### Added

-Add the exceptions.py file for exceptions that players may have.


# [0.2.6] - 2024-09-12

### Added

-After many complications I managed to get the Pawn capture to work and I know it because all the Tests that I did previously run, that does not mean that perhaps in the future I will add more tests.

# [0.2.5] - 2024-09-11

### Added

-I started to try to add the movements of the capture and collision pawn, the problem is that they are still not 100% working.

# [0.2.4] - 2024-09-10

### Added

-I added a couple of Tests for the pawn movements but it is getting complicated for me to do the movements correctly, especially the capture and the collision.

# [0.2.3] - 2024-09-05

### Added

-Apply the new functions to the Horse piece and it can now capture and collide correctly, and it passed all the tests I did yesterday.

# [0.2.2] - 2024-09-04

### Added

-Today I could refactory the Horse tests inclduding validar_colision and validar_captura with the aim of be able to add Horse movements in the future.

# [0.2.1] - 2024-09-03

### Added


-Tonight I finished refactoring the code of the King piece so that it passes the tests correctly. What I added were the "validate_capture" and "validate_collision" functions and edited the "basic_movements_of_kings" function.

# [0.2.0] - 2024-09-02

### Added

-Today I did the King piece tests which check the capture of pieces of the opposite color and collision with pieces of the same color.


# [0.1.9] - 2024-09-01

### Added

-Finish Queens' movements, now she has passed all the tests and I am ready to continue with the capture and collision mechanics of the "King, Horse and Pawn" pieces.

# [0.1.8] - 2024-08-31

### Added

-Add the Queens Tests and now all that remains is to correct some small details of the functions so that the tests run correctly and with that the Queen piece would finish.


# [0.1.7] - 2024-08-30

### Added

-I completed the Capture and Collision functions of "Alfils" and they fit perfectly with the tests I did in the last Commit. Now with Rook and Alfils finished I can continue with Queens.



# [0.1.6] - 2024-08-29

### Added

-The Obstruction and Capture tests
-Add the Alfils Tests to then implement the Alfils' movements and then do the Queens tests and its code since Queens depends on Rook and Alfils.


# [0.1.5] - 2024-08-28

### Added

-I added the tests and refactored my Rook code so that it can also move, capture and collide.

 -So that my Rook code works and that in addition to moving, colliding and capturing
    I had to make big changes to my code and split it into 3 main functions
    (basic movements, validate collision, validate capture)
    So instead of making it go down the row and column, separate it into 4 sections 
    left right up and down.

    First I define the range it will cover and how often and to what extent.
    Second valid possible collisions.
    Third valid captures.
    Fourth returns all moves.

    Although by making these changes and having my Queen piece related to the Rook's movements, the Test_Queens are now not working for me, so I am going to try to correct it in the following previews.


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
