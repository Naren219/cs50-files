import csv
import sys

def main():
    if len(argv) != 3:
        sys.exit("Usage: python dna.py FILENAME(CSV) sequence.txt")

    people = {}
    with open("argv[1]", "r") as file:
        reader = csv.DictReader(file)
        next(file)
        for row in reader:
            name = row['name']
            row['']
