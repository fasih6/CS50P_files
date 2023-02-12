from sys import argv
import csv

if len(argv) > 3:
    exit("Too many command-line arguments")
elif len(argv) < 3:
    exit("Too few command-line arguments")
else:
    try:
        y, z = argv[1].split(".")
        if z != "csv":
            print("Could not read", argv[1])
            exit()
    except:
        print("Could not read", argv[1])
        exit()

table = []
with open(argv[1],"r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # first, last = row["name"].split(",")
        # last = last.strip()
        last, first = row["name"].split(",")
        first = first.strip()
        house = row["house"]
        table.append({"first": first, "last": last, "house": house})

with open(argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first","last","house"])
    writer.writeheader()
    for item in table:
        writer.writerow(item)