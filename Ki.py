""" This module contains the AI of the Game "Vier gewinnt mal anders"

"""
import random
import deepcopy from copy

import GameCheck from GameCheck

__author__ = "6345060 Nico Kotlenga, 6404053: Tim Geier"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de, uni@tim-geier.de"

class AI:

    def __init__(self, currentGameField):
        """ This method will be called during the initialization of the AI
            class. The parameter is the reference to the current game field

        """
        self.currentGameField = currentGameField;

    def get_next_move(self):
        """ This method will return a numeric value which contains the number
            of row, which the computer wants to play next

        """


    def  __checkForThreeCol(self, cuttedGameField):
        """Check for a possibility to get three in a col (this increases the
            possibility for a win)
            
        """
        countRows = len(cuttedGameField)
        countCol = len(cuttedGameField[0])

        for x in range(0, countCol, 1):
            maxYCount = 0
            for y in rnage(0, countRows, 1):
                if(cuttedGameField[y][x] == 2):
                    maxYCount += 1
                else:
                    if(maxYCount == 2):

    def  __checkForThreeRow(self, cuttedGameField):
        """ Check for a possibility to get three in a row (this increases the
            possibility for a win)

        """
        countRows = len(cuttedGameField)
        countCol = len(cuttedGameField[0])

        for y in range(0, countRows, 1):
            maxXCount = 0
            for x in range(0, countCol, 1):
                if(cuttedGameField[y][x] == 2):
                    maxXCount += 1
                else:
                    if(maxXCount == 2):
                        leftFree = False;
                        rightFree = False
                        if(x - 3 >= 0 and cuttedGameField[y][x - 3] == 0):
                            leftFree = True
                        if(x + 1 < len(countCol) and \
                        cuttedGameField[y][x + 1] == 0):
                            rightFree = True

                         int prefferedSite = random.randint(0,1) # 0left 1right
                         if(prefferedSite == 0 and leftFree == True):
                             return x - 3
                         if(prefferedSite == 1 and rightFree == True):
                             return x + 1
                    maxXCount = 0

        return None


    def __checkForWin(self, cuttedGameField):
        """ This method checks whether a win is possible in the next round.
            If yes, it will return a numeric value with the col. Otherwise
            it will return None.
        """

        countRows = len(cuttedGameField)
        countCol = len(cuttedGameField[0])

        for y in range(0, countRows, 1):
            maxInARow = 0
            for x in range(0, countCol, 1):
                if(cuttedGameField[y][x] == 2):
                    maxInARow += 1
                else:
                    if(maxInARow > 1):
                        #now drop a virtual coin
                        for k in range(0, maxInARow, 1):
                            maybeWin = self.__virtualMove((x - (k + 1)), \
                            deepcopy(cuttedGameField)))

                            if(maybeWin):
                                return (x - (k + 1))
                    maxInARow = 0
        return None

    def __virtualMove(self, col, copiedGameField):
        """ this method uses a copy of the gamefield to make a virtual move.
            It will return true if after the move the game is won.

        """

        for y in range(0, len(copiedGameField), 1):
            if(copiedGameField[y][col] == 0):
                copiedGameField[y][col] = 1
                cur_game_checker = GameCheck(copiedGameField)
                if(cur_game_checker.is_game_finish(copiedGameField) == 2):
                    return True
        return False
