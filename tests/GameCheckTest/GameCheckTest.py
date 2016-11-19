""" This module contains the Testcases for the class Game Check

"""
import GameCheck
import copy

def testCaseFor_is_game_finish():
    """ this method tests the methode "is_game_finish" of the module
        GameCheck.

    """

    print("Checking functionality of is_game_finish......")
    # creating a empty array
    cur_game_field = []
    for i in range(0, 3, 1):
        temp = []
        for k in range(0, 3, 1):
            temp.append(0)
        cur_game_field.append(temp)

    cur_game_check = GameCheck.GameCheck(cur_game_field)

    # empty array means, that nobody has won the game --> case 1
    print("No one has won the game ---> ", \
    str(cur_game_check.is_game_finish()))

    # fill it with a win of player 1
    cur_game_field[0][0] = 1
    cur_game_field[0][1] = 1
    cur_game_field[0][2] = 1
    cur_game_field[1][0] = 1

    print("Player one has won the game ---> ", \
    str(cur_game_check.is_game_finish()))

    # fill it with a win of player 2
    cur_game_field[0][0] = 2
    cur_game_field[0][1] = 2
    cur_game_field[0][2] = 2
    cur_game_field[1][0] = 2

    print("Player two has won the game ---> ", \
    str(cur_game_check.is_game_finish()))




def testCaseFor__check_for_win_of(n):
    """ this method tests the method "check_for_win_of" of the module
        GameCheck. The parameter n contains the size of thee field
        n have to higher than 2
    """
    if(n < 3):
        return # break the function because of a to small n

    # win cases
    print("Check win cases... \n-------------------")
    for i in range(0, n, 1):
        currentField = []
        for fillY in range(n):
            tempList = []
            for fillX in range(n):
                tempList.append(0)
            currentField.append(tempList)
        for k in range(0, n, 1):
            if(k == (n - 1) and (i + 2) < n):
                copiedField = copy.deepcopy(currentField)
                # must append the x on the left side
                copiedField[i][k - 1] = 1
                copiedField[i + 1][k] = 1
                copiedField[i + 2][k] = 1
                copiedField[i][k] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i + 1), ",", str(k),"][", str(i + 2), ",", str(k), \
                "][",str(i), ",", str(k - 1), "] -----> ", str(result))
            if(k == (n - 1) and (i - 2) >= 0):
                copiedField = copy.deepcopy(currentField)
                # must append the x on the left side
                copiedField[i][k] = 1
                copiedField[i - 1][k] = 1
                copiedField[i - 2][k] = 1
                copiedField[i][k - 1] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i - 1), ",", str(k),"][", str(i - 2), ",", str(k), \
                "][",str(i), ",", str(k - 1), "] -----> ", str(result))
            if(k != (n - 1) and (i + 2) < n):
                copiedField = copy.deepcopy(currentField)
                # must append the x on the right side
                copiedField[i][k] = 1
                copiedField[i + 1][k] = 1
                copiedField[i + 2][k] = 1
                copiedField[i][k + 1] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i + 1), ",", str(k),"][", str(i + 2), ",", str(k), \
                "][",str(i), ",", str(k + 1), "] -----> ", str(result))

            if(k != (n - 1) and (i - 2) >= 0):
                copiedField = copy.deepcopy(currentField)
                # must append the x on the right side
                copiedField[i][k] = 1
                copiedField[i - 1][k] = 1
                copiedField[i - 2][k] = 1
                copiedField[i][k + 1] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i - 1), ",", str(k),"][", str(i - 2), ",", str(k), \
                "][",str(i), ",", str(k + 1), "] -----> ", str(result))

    # loose cases
    print("Check loose cases...\n--------------")
    for i in range(0, n, 1):
        currentField = []
        for fillY in range(n):
            tempList = []
            for fillX in range(n):
                tempList.append(0)
            currentField.append(tempList)
        for k in range(0, n, 1):
            if(k == (n - 1) and (i + 1) < n):
                copiedField = copy.deepcopy(currentField)
                # must be append on the left side
                copiedField[i][k] = 1
                copiedField[i][k - 1] = 1
                copiedField[i + 1][k] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i + 1), ",", str(k),"][",str(i), ",", str(k - 1),\
                "] -----> ", str(result))
            if(k == (n - 1) and (i - 1) >= 0):
                copiedField = copy.deepcopy(currentField)
                # must append x on the left side
                copiedField[i][k] = 1
                copiedField[i][k - 1] = 1
                copiedField[i - 1][k] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i - 1), ",", str(k),"][",str(i), ",", str(k - 1),\
                "] -----> ", str(result))
            if(k != (n - 1) and (i + 1) < n):
                copiedField = copy.deepcopy(currentField)
                # msut append x on the right side
                copiedField[i][k] = 1
                copiedField[i][k + 1] = 1
                copiedField[i + 1][k] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i + 1), ",", str(k),"][",str(i), ",", str(k + 1),\
                "] -----> ", str(result))
            if(k != (n - 1) and (i - 1) >= 0):
                copiedField = copy.deepcopy(currentField)
                # must append x on the right side
                copiedField[i][k] = 1
                copiedField[i][k + 1] = 1
                copiedField[i - 1][k] = 1

                current_game_check = GameCheck.GameCheck(copiedField)
                result = current_game_check.check_for_win_of(1, copiedField)

                print("Occupied fields : [", str(i), ",", str(k), "]", \
                "[", str(i - 1), ",", str(k),"][",str(i), ",", str(k + 1),\
                "] -----> ", str(result))

print("Wie groß soll das Spielfeld werden?")
number = int(input("n:= "))
testCaseFor__check_for_win_of(number)
testCaseFor_is_game_finish()
