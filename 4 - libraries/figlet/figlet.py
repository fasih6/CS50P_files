from sys import argv
from pyfiglet import Figlet      # pip install pyfiglet

x = ""

if len(argv) == 1:
    x = input("Input: ")
    f = Figlet(font='slant')
    print(f.renderText(x))
    exit()

elif len(argv) == 3:
    if argv[1] == "-f":
        try:
            f = Figlet(font=argv[2])
            x = input("Input: ")
            print("Output: \n")
            print(f.renderText(x))
        except:
            exit("Invalid usage")
    else:
        exit("Invalid usage")
else:
    exit("Invalid usage")

# f = Figlet(font='rectangles')
# print(f.renderText('text to render'))