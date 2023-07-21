from cs50 import get_int

number_int = get_int("Number: ")
number = str(number_int)
length = len(number)

if (length % 2 == 0):
    for i in range(number_int[length - 2], number_int[0], -2):
        numberx2[i] = 2 * number_int[i]

    for j in numberx2:
        sum1 = 0
        sum1 += numberx2[j]

    for n in range(number_int[length - 1], number_int[1], -2):
        sum2 = 0
        sum2 += number_int[n]

else:
    for i in range(number_int[length - 2], number_int[1], -2):
        numberx2[i] = 2 * number_int[i]

    for j in numberx2:
        sum1 = 0
        sum1 += numberx2[j]

    for n in range(number_int[length - 1], number_int[0], -2):
        sum2 = 0
        sum2 += number_int[n]


check = (sum1 + sum2) % 10
length_ch = len(str(check))

if check[length_ch - 1] != 0:
    print("INVALID")
elif len(number) == 15 and number[0] == 3 and number[1] == 4 or 7:
    print("AMEX")
elif len(number) == 16 and number[0] == 5 and number[1] == 1 or 2 or 3 or 4 or 5:
    print("MASTERCARD")
elif len(number) == 13 or 16 and number[0] == 4:
    print("VISA")
else:
    print("INVALID")




