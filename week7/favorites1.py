import csv

from cs50 import SQL

open("sciences.db", "w").close()
db = SQL("sqlite:///sciences.db")

db.execute("CREATE TABLE science (id INTEGER, title TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE subject (science_id INTEGER, subject TEXT, FOREIGN KEY(science_id) REFERENCES science(id))")

with open("What type of science do you like_ (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        science = row["science"].strip().upper()
        db.execute("INSERT INTO sciences (science) VALUES(?)", science)
        for subject in row["subject"].split(","):
            db.execute("INSERT INTO subject (science_id, subject) VALUES(?, ?)", id, subject)