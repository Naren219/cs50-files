from cs50 import get_int

while 0 < height < 9:
    height = get_int("Height: ")
    for row in range(height):
        for column in range(height):
            if (row + column < height - 1):
                print(" ")
            else:
                print("#")