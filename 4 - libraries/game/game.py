import random
import sys

x = -1
while x <= 0:
    try:
        x = int(input("Level: "))
    except:
        pass


y = random.randint(1, x)
z = -1

while z <= 0:
    try:
        z = int(input("Guess: "))
        if z == y:
            print("Just right!")
            break
        elif z > y:
            print("Too large!")
            z = -1
            continue
        else:
            print("Too small!")
            z = -1
            continue
    except:
        pass


