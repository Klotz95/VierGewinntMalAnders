""" This module checks the gamestate of "vier gewinnt (mal anders)"

"""

__author__ = "123456:6345060 Nico Kotlenga, 6404053: Tim Geier"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni frankfurt.de, uni@tim-geier.de"


class GameCheck:

    def __init__(self, currentGameField):
        """ This method will be called during the initialization of a new
            object of this class. currentGameField contains a two dimesnional
            array which describes the current state of the game

        """
        self.__currentGameField = currentGameField


    def is_game_finish(self):
        """This method checks if the current game is finish and returns a
           boolean value

        """
        # cut the game field (this will improve the performance of the check)

        cuttedGameField = [self.__currentGameField[0]]

        for i in rage(1, len(self.__currentGameField), 1):
            currentRow = self.__currentGameField[i]
            for k in currentRow:
                if(k is not None):
                    cuttedGameField.append(currentRow)
                    break

        if(len(cuttedGameField) >= 2):
            return __check_for_Win_Of("X" , cuttedGameField) /
                   or __check_for_Win_Of("O", cuttedGameField)

        return False

    def __check_for_Win_Of(playerSign, cuttedGameField):
        """This method checks if a specific player has won the game.
           Therefor the method has the parameter playerSign which has to be a
           string and contains the player Symbol like "X" , "O"...

        """
