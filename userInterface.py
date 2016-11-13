import time
import os

logo = """
██╗  ██╗     ██████╗ ███████╗██╗    ██╗██╗███╗   ██╗███╗   ██╗████████╗
██║  ██║    ██╔════╝ ██╔════╝██║    ██║██║████╗  ██║████╗  ██║╚══██╔══╝
███████║    ██║  ███╗█████╗  ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║   ██║   
╚════██║    ██║   ██║██╔══╝  ██║███╗██║██║██║╚██╗██║██║╚██╗██║   ██║   
     ██║    ╚██████╔╝███████╗╚███╔███╔╝██║██║ ╚████║██║ ╚████║   ██║   
     ╚═╝     ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                      
"""


data = [[0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0]]

def printGame():
    os.system("cls")
    print("| 1 | 2 | 3 | 4 | 5 | 6 |")
    print("-------------------------")
    for i in range(0,8):
        for j in range(0,6):
            if j == 0:
                print("|", end="")
            if data[i][j] == 0:
                print("   |", end="")
            elif data[i][j] == 1:
                print(" X |", end="")
            elif data[i][j] == 2:
                print(" O |", end="")
        print()
    print("-------------------------")

player = False

def dropCoin(col):
    for i in range(7,-1,-1):
        if not data[i][col]:
            if player:
                data[i][col] = 1
                break
            else:
                data[i][col] = 2
                break
    else:
        pass

def checkWinner():
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            try:
                if data[i][j] == data[i - 1][j] == data[i -2][j] == data[i][j + 1] and data[i][j] != 0:
                    print("X" if data[i][j] == 1 else "O", "hat gewonnen")
                    time.sleep(2)
            except:
                pass

print(logo)
time.sleep(0.5)

while 1:

    printGame()
    s = input("Bitte Spalte eingeben: ")
    try:
        s = int(s)
    except:
        print("Falsche Eingabe")
        break
    if s < 1: s=1
    if s>6:s=6
    player =  not player
    dropCoin(int(s)-1)
    printGame()
    checkWinner()
