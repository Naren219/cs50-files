from array import *
from random import seed
from random import randint
"""
    
"""

seed(1)

def printboard() 
    print("|---|---|---|")
    
arr = [[0]*9]*9
def main():
    for r in arr:
        for c in r:
            number[i] = randint(0, 10)
            if equals3(r):
                print()
                print(c, end = "_")
            elif equals3(c):
                print(c, end = "|")
            else:
                print(c,end = " ")
        print()
def equals3(x):
    if x == 3 or x == 6 or x == 9:
        return true
    #return false

if __name__ == "__main__":
    main()

