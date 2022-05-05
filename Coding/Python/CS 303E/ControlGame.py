# File: ControlGame.py
# Student:
# UT EID:
# Course Name: CS303E
#
# Date:
# Description of Program:

MAX_TURNS = 64
EMTPY_BOARD = [['.' for col in range(8)] for row in range(8)]
PLAYER = "Red"



class ControlGame:

    def __init__(self, turnsToPlay=MAX_TURNS):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].
        self.turnsToPLay = turnsToPlay
        return

    def __str__(self):
        # Permit displaying the header "Current board is:" following by the
        # board.
        def board():
            num = ["0", "1", "2", "3", "4", "5", "6", "7"]
            print('  ', end='')
            for col in range(8):
                print(num[col], end=' ')

            print()

            for row in range(8):
                print(num[row], end=" ")
                for i in EMTPY_BOARD:
                    print(".", end=" ")
                print()
        self.__board = board()
        return

    def getCurrentPlayer(self):
        # Return the current player, 'Red' or 'Blue'
        return PLAYER

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and
        # vice versa.
        if self.getCurrentPlayer() == "Blue":
            PLAYER = "Red"
        elif self.getCurrentPlayer() == "Red":
            PLAYER = "Blue"
        return PLAYER

    def getBoardState(self):
        # Return the current board.
        pass

    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value
        # indicating whether or not the turn occurred.
        self.row = row
        self.col = col
        return

    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea
        # to write subsidiary functions for this.
        pass
