import math

degree = int(input("Degree: "))
mod = int(input("Mod: "))

print("Vertical: ", round(math.sin(degree)*mod*10)/10)
print("Horizontal: ", round(math.cos(degree)*mod*10)/10)