from sys import argv
x = 0
if len(argv) > 2:
    exit("Too many command-line arguments")
elif len(argv) < 2:
    exit("Too few command-line arguments")
else:
    try:
        y, z = argv[1].split(".")
        if z != "py":
            exit("Not a Python file")
    except:
        exit("Not a Python file")
    try:
        with open(argv[1],"r") as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#") == 0 and len(line) > 0: # if line doesnot start with "#"
                    x += 1
    except FileNotFoundError:
        exit("File does not exist")

print(x)