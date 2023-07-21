from cs50 import get_int

x = get_int("Positive Integer: ")

def fact(x):
  if x != 1:
    return x * fact(x - 1)
  else:
    return 1

print("" + str(fact(x)))

