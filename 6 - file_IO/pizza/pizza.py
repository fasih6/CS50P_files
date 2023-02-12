from sys import argv
import csv
from tabulate import tabulate

if len(argv) > 2:
    exit("Too many command-line arguments")
elif len(argv) < 2:
    exit("Too few command-line arguments")
else:
    try:
        y, z = argv[1].split(".")
        if z != "csv":
            exit("Not a CSV file")
    except:
        exit("Not a CSV file")

table = []
with open(argv[1],"r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        table.append(row)

print(tabulate(table, headers="keys", tablefmt="grid"))