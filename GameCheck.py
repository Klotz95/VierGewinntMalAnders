""" This module checks the gamestate of "vier gewinnt (mal anders)"

"""

__author__ = "6345060 Nico Kotlenga, 6404053: Tim Geier"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de, uni@tim-geier.de"


class GameCheck:

    def __init__(self, currentGameField):
        """ This method will be called during the initialization of a new
            object of this class. currentGameField contains a two dimesnional
            array which describes the current state of the game

        """
        self.__currentGameField = currentGameField


    def is_game_finish(self):
        """This method checks if the current game is finish and returns 0
            if the game is still in progress. Otherwise it will return the
            number of the player who has won the match
        """
        # cut the game field (this will improve the performance of the check)

        cuttedGameField = [self.__currentGameField[0]]

        for i in range(1, len(self.__currentGameField), 1):
            currentRow = self.__currentGameField[i]
            for k in currentRow:
                if(k is not None):
                    cuttedGameField.append(currentRow)
                    break

        if(len(cuttedGameField) >= 2):
            if(self.__check_for_win_of(1, cuttedGameField)):
                return 1
            elif(self.__check_for_win_of(2, cuttedGameField)):
                return 2

        return 0




    def __check_for_win_of(self, playerSign, cuttedGameField):
        """This method checks if a specific player has won the game.
           Therefor the method has the parameter playerSign which has to be a
           string and contains the player Symbol like "X" , "O"...

        """

        countOfLines = len(cuttedGameField)
        countOfRows = len(cuttedGameField[0]) # countOfLines >=2 no exception
        for y in range(countOfLines):
            currentCountOfSignsInARow = 0
            for x in range(countOfRows):
                if(cuttedGameField[y][x] == playerSign):
                     currentCountOfSignsInARow += 1
                else:
                     if(currentCountOfSignsInARow == 2):
                         # check for two bot and top
                         if(countOfLines - (y + 1) >= 2):
                             # prevent index out of range exception
                             if((cuttedGameField[y + 1][x - 2] == playerSign \
                             and cuttedGameField[y + 2][x - 2] == playerSign)\
                             or (cuttedGameField[y + 1][x - 1] == playerSign \
                             and cuttedGameField[y + 2][x - 1] == playerSign)):
                                return True
                         if(y >= 2):
                             if((cuttedGameField[y - 1][x - 2] == playerSign \
                             and cuttedGameField[y - 2][x - 2] == playerSign)\
                             or (cuttedGameField[y - 1][x - 1] == playerSign \
                             and cuttedGameField[y - 2][x - 1] == playerSign)):
                                return True

                     elif(currentCountOfSignsInARow == 3):
                         if(countOfLines - (y + 1) >= 1):
                             for i in range(3, 0, - 2):
                                 if(cuttedGameField[y + 1][x - i] == \
                                 playerSign):
                                    return True
                         if(y >= 1):
                             for i in range(3, 0, - 2):
                                 if(cuttedGameField[y - 1][x - i] == \
                                 playerSign):
                                    return True
                         if(countOfLines - (y + 1) >= 2 and \
                         cuttedGameField[y + 1][x - 2] == playerSign and \
                         cuttedGameField[y + 2][x - 2] == playerSign):
                            return True
                         if(y >= 2 and cuttedGameField[y - 1][x - 2] == \
                         playerSign and cuttedGameField[y - 2][x - 2] == \
                          playerSign):
                            return True

                     elif(currentCountOfSignsInARow > 3):
                         for i in range(currentCountOfSignsInARow, 0 , -1):
                             if(countOfLines - (y + 1) >= 1):
                                 if(cuttedGameField[y + 1][x - i] == \
                                 playerSign):
                                    return True
                             if(y >= 1):
                                 if(cuttedGameField[y - 1][x - i] == \
                                 playerSign):
                                    return True

                     # reset currentCountOfSignsInARow
                     currentCountOfSignsInARow = 0
        #if no combination has been found
        return False
