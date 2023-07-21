from array import *

arr = [[0]*3]*3
whole = [[arr]*3]*3
def main():
    for row in whole:
        for column in row:
            printarr()
            vertline()
            print()
        print()

def printarr():
    for r in arr:
        for c in r:
            print(c,end = arr)
        print()

def vertline():
    for i in range(3):
        print("   0")
if __name__ == "__main__":
    main()

