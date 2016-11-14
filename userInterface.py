# coding: utf-8

import time
import os
import random
#import ai.py
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

def initGame(target_list):
    global actual_player
    actual_player = 1
    if len(target_list) < 1:
        for i in range(GRID_HEIGHT):
            temp_list = []
            for j in range(GRID_WIDTH):
                temp_list.append(0)
            target_list.append(temp_list)
    else:
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                target_list[i][j] = 0

# endregion

# region "print game_data to console"

def printGame():
    clearConsole()
    game_field = "|"
    for i in range(GRID_WIDTH):
        game_field += " " + str(i+1) + " |"
    game_field += "\n"
    game_width = len(game_field) - 1
    for i in range(game_width):
        game_field += "-"
    game_field += "\n"
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if j == 0:
                game_field += "|"
            game_field += " "
            if game_data[i][j] == 0:
                game_field += " "
            elif game_data[i][j] == 1:
                game_field += PLAYER1_SYMBOL
            elif game_data[i][j] == 2:
                game_field += PLAYER2_SYMBOL
            game_field += " |"
        game_field += "\n"
    
    for i in range(game_width):
        game_field += "-"
    game_field += "\n"

    print(game_field)

def clearConsole():
    os.system("cls")

# endregion

# region "dropCoin"

actual_player = 1

def drop_coin(col):
    global actual_player
    for i in range(GRID_HEIGHT - 1, -1, -1):
        if not game_data[i][col]:
            if actual_player == 1:
                game_data[i][col] = 1
                actual_player = 2
                return True
            elif actual_player == 2:
                game_data[i][col] = 2
                actual_player = 1
                return True
    else:
        return False

# endregion

# region "game logic/main menu"
"""

possible game_state's:
    0   main menu
    1   singleplayer, game running
    2   multiplayer, game running
"""

def getUserInput():
    global game_state
    temp_input = input("Bitte Spalten Nr. eingeben: ")
    if temp_input == "exit":
        clearConsole()
        game_state = 0
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

    a = input("Bitte Auswahl treffen: ")
    if a == "exit":
        break
    else:
        if a.isnumeric():
            s = int(a)
            game_state = s
        else:
            print("Falsche Eingabe")
            continue

    initGame(game_data)

    while game_state == 2:
        printGame()
        print("Spieler", actual_player, "ist am Zug")
        s = getUserInput()
        if s < 0:
            continue
        drop_coin(int(s)-1)
        # TODO: check State

    while game_state == 1:
        printGame()
        if actual_player == 1:
            s = getUserInput()
            if s < 0:
                continue
            if not drop_coin(int(s)-1): continue
        else:
            print("Computer denkt...")
            # TODO: AI Implementieren
            while not drop_coin(random.randint(0, GRID_WIDTH-1)):
                pass
            time.sleep(1)
        # TODO: check State
   
# endregion