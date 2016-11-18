"""Simple implementation of modified game connect four with console interface
program for EPR 03
"""

__author__ = "6345060 Nico Kotlenga, 6404053: Tim Geier"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni frankfurt.de, uni@tim-geier.de"


import time
import os
import random
import platform
import GameCheck
import ai
#import gameCheck.py

# region "constants / settings"

PLAYER1_SYMBOL = "X"
PLAYER2_SYMBOL = "O"

GRID_WIDTH = 6
GRID_HEIGHT = 8

LOGO = """
██╗  ██╗     ██████╗ ███████╗██╗    ██╗██╗███╗   ██╗███╗   ██╗████████╗
██║  ██║    ██╔════╝ ██╔════╝██║    ██║██║████╗  ██║████╗  ██║╚══██╔══╝
███████║    ██║  ███╗█████╗  ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║   ██║
╚════██║    ██║   ██║██╔══╝  ██║███╗██║██║██║╚██╗██║██║╚██╗██║   ██║
     ██║    ╚██████╔╝███████╗╚███╔███╔╝██║██║ ╚████║██║ ╚████║   ██║
     ╚═╝     ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝

"""

MENU = """
Hauptmenü:

    Das Spiel kann jederzeit durch Eingabe von 'exit' beendet werden.
    Oder mit 'restart' neu gestartet werden

    Einspieler Modus starten:   1
    Zweispieler Modus starten:  2

    Programm beenden:           exit

"""

#endregion

# region "initialize game_data list"
game_data = []
game_checker = GameCheck.GameCheck(game_data)
ai = ai.ai(game_data)
def initGame(target_list):
    """Initialize target_list
        Create GRID_HEIGHT lists with GRID_WIDTH items
        If target_list is already defined, set every item to 0
    """
    global gActualPlayer
    gActualPlayer = 1
    if len(target_list) < 1:
        for i in range(GRID_HEIGHT):
            temp_list = []
            for j in range(GRID_WIDTH):
                temp_list.append(0)
            target_list.append(temp_list)
    else:
        for curr_row in range(GRID_HEIGHT):
            for current_column in range(GRID_WIDTH):
                target_list[curr_row][current_column] = 0

# endregion

# region "print game_data to console"

def printGame():
    """print game_data formatted as table to console
        generates something like:
        | 1 | 2 | 3 |
        -------------
        |   |   |   |
        |   |   |   |
        |   | X |   |
        | X | O |   |
        -------------
    """
    clearConsole()
    game_field = "|"
    for curr_row_number in range(1, GRID_WIDTH + 1):
        game_field += " " + str(curr_row_number) + " |"
    game_field += "\n"
    game_width = len(game_field) - 1
    for i in range(game_width):
        game_field += "-"
    game_field += "\n"
    for curr_row in range(GRID_HEIGHT):
        for current_column in range(GRID_WIDTH):
            if current_column == 0:
                game_field += "|"
            game_field += " "
            if game_data[curr_row][current_column] == 0:
                game_field += " "
            elif game_data[curr_row][current_column] == 1:
                game_field += PLAYER1_SYMBOL
            elif game_data[curr_row][current_column] == 2:
                game_field += PLAYER2_SYMBOL
            game_field += " |"
        game_field += "\n"

    for i in range(game_width):
        game_field += "-"
    game_field += "\n"

    print(game_field)

def clearConsole():
    """clears the console window
       different implementation for Windows and Unix
    """
    currentOS = platform.system()

    if(currentOS == "Windows"):
        os.system("cls")
    else:
        os.system("clear")





# endregion

# region "dropCoin"

gActualPlayer = 1

def drop_coin(col):
    """tries to put a coin in column col
        col needs to be the column index beginning at 0
    """
    global gActualPlayer
    for curr_row in range(GRID_HEIGHT - 1, -1, -1):
        if not game_data[curr_row][col]:
            if gActualPlayer == 1:
                game_data[curr_row][col] = 1
                gActualPlayer = 2
                return True
            elif gActualPlayer == 2:
                game_data[curr_row][col] = 2
                gActualPlayer = 1
                return True
    else:
        return False

# endregion

# region "game logic/main menu"
"""
possible values for gGameState:
    0   main menu
    1   singleplayer, game running
    2   multiplayer, game running
"""

def getUserInput():
    """processes user input
        asks user for column number to put coin to
        processes 'exit' and 'restart' commands
    """
    global gGameState
    temp_input = input("Bitte Spalten Nr. eingeben: ")
    if temp_input == "exit":
        clearConsole()
        gGameState = 0
        return -1
    elif temp_input == "restart":
        initGame(game_data)
        return -1
    try:
        temp_input = int(temp_input)
        if temp_input < 1: temp_input = 1
        elif temp_input > GRID_WIDTH: temp_input = GRID_WIDTH
        return temp_input
    except:
        print("Falsche Eingabe")
        return -1

while 1:
    clearConsole()
    print(LOGO)
    print(MENU)

    temp_input = input("Bitte Auswahl treffen: ")
    if temp_input == "exit":
        break
    else:
        if temp_input.isnumeric():
            gGameState = int(temp_input)
        else:
            print("Falsche Eingabe")
            continue

    initGame(game_data)

    while gGameState == 2:
        printGame()
        print("Spieler", gActualPlayer, "ist am Zug")
        target_column = getUserInput()
        if target_column < 0:
            continue
        drop_coin(int(target_column)-1)
        curGameState = game_checker.is_game_finish()
        if(curGameState != 0):
             input("Spieler " + str(curGameState) + " hat gewonnen...")
             gGameState = 0

    while gGameState == 1:
        printGame()
        if gActualPlayer == 1:
            target_column = getUserInput()
            if target_column < 0:
                continue
            if not drop_coin(int(target_column)-1): continue
        else:
            print("Computer denkt...")
            # TODO: AI Implementieren
            while not drop_coin(ai.get_next_move()):
                pass
          
        # check for win
        curGameState = game_checker.is_game_finish()
        if(curGameState != 0):
            if(curGameState == 1):
                input("Glückwunsch, sie haben gewonnen...")
            else:
                input("Sie haben verloren. Viel Glück beim nächsten Spiel")
            gGameState = 0

# endregion
