from cs50 import get_int

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

place1 = []
place2 = []
print("You choose a spot to move your noughts or crosses using your keypad.")
print("Player 1 is X and Player 2 is O")

def main():
    while ('1','2','3' or '4','5','6' or '7','8','9' or '7','4','1' or '8','5','2' or '9','6','3' or '7','5','3' or '9','5','1' not in place1 or place2):
        printboard()

        placeX = get_int("Player 1:")
        if 0 < placeX < 10:
            if incorrectmoveX(placeX) == false:
                place1.append(placeX)
                board['placeX'] = 'X'
            else:
                print("Place character at different slot.")
        else:
            print("Enter number from 1-9 to choose your spot")

        printboard()

        placeO = get_int("Player 2:")
        if 0 < placeO < 10:
            if incorrectmoveO(placeO) == false:
                place2.append(placeO)
                board['placeO'] = 'O'
            else:
                print("Place character at different slot.")
        else:
            print("Enter number from 1-9 to choose your spot")

        printboard()

    elif ('1','2','3' or '4','5','6' or '7','8','9' or '7','4','1' or '8','5','2' or '9','6','3' or '7','5','3' or '9','5','1' in place1):
        print("Player 1 won!")
    elif ('1','2','3' or '4','5','6' or '7','8','9' or '7','4','1' or '8','5','2' or '9','6','3' or '7','5','3' or '9','5','1' in place2):
        print("Player 2 won!")
    else:
        print("It's a tie")

def printboard():
    print(board['7'] + "|" + board['8'] + "|" + board['9'])
    print("-+-+- ")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-+-+- ")
    print(board['1'] + "|" + board['2'] + "|" + board['3'])

def incorrectmoveX(placeX):
    for i in range(len(place1)):
        if place1[i] == placeX or place2[i] == placeX:
            return true
        else:
            return false
    for j in range(len(place2)):
        if place1[i] == placeX or place2[i] == placeX:
            return true
        else:
            return false

def incorrectmove0(placeO):
    for i in range(len(place1)):
        if place1[i] == placeO or place2[i] == placeO:
            return true
        else:
            return false
    for j in range(len(place2)):
        if place1[i] == placeO or place2[i] == placeO:
            return true
        else:
            return false

main()
