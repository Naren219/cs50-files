import csv

sciences = {}

with open("What type of science do you like_ (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        science = row["science"].strip().upper()
        if science not in sciences:
            sciences[science] = 1
        sciences[science] += 1


for science in sorted(sciences, key=lambda science: sciences[science], reverse=True):
    print(science, sciences[science])