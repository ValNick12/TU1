from msvcrt import kbhit
import os


import os
player1 = str(input("Player 1 - Choose between Rock, Paper and Scissors (type r/p/s): "))
os.system("cls")
player2 = str(input("Player 2 - Choose between Rock, Paper and Scissors (type r/p/s): "))
inputlist = (player1, player2)
if player1 == player2:
    print("Remy")
elif inputlist in [("p", "r"), ("r", "s"), ("s", "p")]:
    print("Congrats Player 1!!!")
elif inputlist in [("r", "p"), ("s", "r"), ("p", "s")]:
    print("Congrats Player 2!!!")
else:
    print("Enter valid arguments!!!")