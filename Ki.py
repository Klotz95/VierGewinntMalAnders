"""Simple implementation of computer opponent

"""

__author__ = "6345060: Nico Kotlenga, 6404053: Tim Geier"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni frankfurt.de, uni@tim-geier.de"
import randomclass ki():    """calculates next move for EPR3 Project    """    def __init__(self, currentGameField):        """ This method will be called during the initialization of a new            object of this class. currentGameField contains a two dimesnional            array which describes the current state of the game        """        self.__currentGameField = currentGameField    def get_next_move(self):        """return collumn index for next move        """        currentGameField = self.__currentGameField        lineLength = len(currentGameField[0])-1        for curr_row in range(len(currentGameField)-1 , -1, -1):            if self.__check_if_row_is_full(currentGameField, curr_row):                continue            else:                three_in_row = self.__check_if_three_in_row(currentGameField, curr_row)                two_in_row = self.__check_if_two_in_row(currentGameField, curr_row)                if three_in_row >= 0:                        try:                        if currentGameField[curr_row+1][three_in_row] == 1:                            continue                        else:                                      return three_in_row                    except IndexError:                        continue                if two_in_row >= 0:                        try:                        if currentGameField[curr_row+1][two_in_row] == 1:                            continue                        else:                                      return two_in_row                    except IndexError:                        continue                for i in range(lineLength):                    if currentGameField[curr_row][i] == 2:                        try:                            if  currentGameField[curr_row][i + 1] == 0:                                return i+1                            elif currentGameField[curr_row][i - 1] == 0:                                return i-1                        except IndexError:                            continue        else:            return(random.randint(0, lineLength))    def __check_if_row_is_full(self, gameField, row):        is_full = True        for curr_collumn in gameField[row]:            if curr_collumn == 0:                is_full = False        return is_full    def __check_if_two_in_row(self, gameField, row):        """returns collumn if 2 coins in a row            returns -1 if not        """        lineLength = len(gameField[0])-1        for curr_collumn in range(lineLength):            if gameField[row][curr_collumn] == 2:                try:                    if random.randint(0,1) == 0:                        if gameField[row][curr_collumn - 1] == 2:                            return curr_collumn                        if gameField[row][curr_collumn + 1] == 2:                            return curr_collumn                    else:                        if gameField[row][curr_collumn + 1] == 2:                            return curr_collumn                        if gameField[row][curr_collumn - 1] == 2:                            return curr_collumn                except IndexError:                    continue        else:            return -1    def __check_if_three_in_row(self, gameField, row):        """return collumn if 3 coins in a row            returns -1 if not        """        lineLength = len(gameField[0])-1        for curr_collumn in range(lineLength):            if gameField[row][curr_collumn] == 2:                try:                    numbers = [[0,1,2],[-2,-1,0]]                    for number in numbers:                        if gameField[row][number[0]] ==  \                            gameField[row][number[1]] == \                            gameField[row][number[2]] == 2:                            return curr_collumn                except IndexError:                    continue        else:            return -1        # region "Tests"

# __init__
#   erwartet das zu nutzende Spielfeld als Argument
#   Wird nichts übergeben, kann die Methode nicht aufgerufen werden

# get_next_move
#   akzepiert keine zusätzlichen Parameter
#   Test:
#       Aufruf bei leerem Feld:
#       --> Gibt zufällige Spalte zurück
#       Aufruf mit nicht leerem Feld:
#       --> Gibt die ausgewählte Spalte zurück
#       Aufruf mit komplett vollem Feld:
#       --> Es wird eine Spalte zurückgegeben,
#        auch wenn der Zug nicht möglich ist.

# __check_if_row_is_full
#   erwartet das Spielfeld sowie die Zeile als Argument
#   Gibt True zurück, falls alle Spalten in der Zeile belegt sind,
#   False falls noch eine Spalte frei ist.
#   Test:
#       Das Spielfeld wird duch die get_next_move Funktion übergeben
#       Die Zeile wird ebenfalls durch get_next_move übergeben,
#        Indexfehler sind somit ausgeschlossen.
#       --> Rückgabe True/False

# endregion