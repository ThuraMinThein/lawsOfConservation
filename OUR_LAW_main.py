from OUR_LAW_Function import *

ch = True 

while ch == True:
    Our_Law_Monmentum()
    ch = input("\nIf you want to exit, Enter 'close'\nOr if you want to start again, Enter 'again' : ")

    if ch =="again":
        ch = True

    elif ch == "close":
        print ("\nThanks you\n")
        ch = False

    else :
        print("\nInvalid: so the program will start again.\n")
        ch = True