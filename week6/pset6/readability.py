from cs50 import get_string

text = get_string("Text: ")

letters = 0
for letter in text:
    while letter.isalnum():
        letters+=1
print(" " + str(letters))