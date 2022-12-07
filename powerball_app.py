# Here i, used colorama library inorder to design the console of the python, all printed value will have different
# colors according to specification
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Here i, imported two classes called WhiteBall and PowerBall that helps to run this powerball project main code
# These classes have their own purposes, their purpose is explained in their own file.
from powerball_utiles import WhiteBall
from powerball_utiles import PowerBall

# This class has the following purposes including printing the results, calling other classes, and most importantly
# make a decision using condition(if, elif and else)
class Prize:
    # here PowerBall class is called to do a random numbers for winning number ranged from 1 to 10
    powerWinner = PowerBall()
    powerWinner.winner()

    # here PowerBall class is called to do a random numbers for lucky numbers ranged from 1 to 10
    powerLucky = PowerBall()
    powerLucky.Lucky()

    # here WhiteBall class is called to do 5 random numbers for winning numbers ranged from 1 to 20
    whitesWinner = WhiteBall()
    whitesWinner.winner()

    # here WhiteBall class is called to do 5 random numbers for lucky numbers ranged from 1 to 20
    whitesLucky = WhiteBall()
    whitesLucky.Lucky()

    # ascending order of white winner numbers
    winnerAscending = whitesWinner.value
    winnerAscending.sort()

    # ascending order of white lucky numbers
    luckyAscending = whitesLucky.value
    luckyAscending.sort()

    # Here is the print part of all results of the program
    print(Fore.GREEN +"_________________________________________________________")
    print("TODAY'S WINNING NUMBER:")
    print(Fore.LIGHTMAGENTA_EX + str(whitesWinner.value ), Fore.YELLOW + str(powerWinner.value))
    print(Fore.GREEN +"_________________________________________________________")

    print("YOUR LUCKY NUMBER:")
    print(Fore.LIGHTMAGENTA_EX + str(whitesLucky.value), Fore.YELLOW + str(powerLucky.value))
    print(Fore.GREEN +"*********************************************************")

    # This counter enable to count the same numbers which are found on both winning white numbers
    # and lucky white numbers
    counterWhite = 0
    for luckyNumber in whitesLucky.value:
        if luckyNumber in whitesWinner.value:
            counterWhite = counterWhite + 1

    # This if, elif and else condition enables the program to decide the amount of the prize that the
    # winner should receive.

    if counterWhite == 5 and (powerWinner.value == powerLucky.value):
        print(counterWhite, "white balls and 1 power ball:Jackpot $324,000,000")
    elif counterWhite == 5 and (powerWinner.value != powerLucky.value):
        print(counterWhite, "white balls and 0 power ball:$1,000,000")
    elif counterWhite == 4 and (powerWinner.value == powerLucky.value):
        print(counterWhite, "white balls and 1 power ball:$10,000")
    elif counterWhite == 4 and (powerWinner.value != powerLucky.value):
        print(counterWhite, "white balls and 0 power ball:$100")
    elif counterWhite == 3 and (powerWinner.value == powerLucky.value):
        print(counterWhite, "white balls and 1 power ball:$100")
    elif counterWhite == 3 and (powerWinner.value != powerLucky.value):
        print(counterWhite, "white balls and 0 power ball:$7")
    elif counterWhite == 2 and (powerWinner.value == powerLucky.value):
        print(counterWhite, "white balls and 1 power ball:$7")
    elif counterWhite == 1 and (powerWinner.value == powerLucky.value):
        print(counterWhite, "white balls and 1 power ball:$4")
    elif counterWhite == 0 and (powerWinner.value == powerLucky.value):
        print(counterWhite, "white balls and 1 power ball:$4")
    else:
        print(Fore.RED +"Try Again!")
