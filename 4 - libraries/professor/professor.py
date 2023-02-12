import random
import sys

isscore = True

def main():
    x = get_level()
    z = 1  # number of Questions
    w = 1  # number of tries
    score = 0
    genrand = True
    while z < 11:
        if genrand == True:
            a, b = generate_integer(x)
            isscore = True
        try:
            print(f"{a} + {b} = ", end="")
            c = int(input(""))
            if a+b == c:
                z += 1
                if isscore:
                    score += 1
                genrand = True
                continue
            elif a+b != c and w == 3:
                print("EEE")
                w = 1
                z += 1
                print(f"{a} + {b} = {a+b}")
                genrand = True
                continue
            elif a+b != c:
                print("EEE")
                isscore = False
                w += 1
                genrand = False
                continue
        except ValueError:
            genrand = False
            print("EEE")
            score -= 1
            pass
        except EOFError:
            print("")
            exit()

    if score < 0:
        score = 0
    print("Score:",score)

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x == 1 or x == 2 or x == 3:
                break
        except ValueError:
            pass
    return x

def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    elif level == 3:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    return a,b


if __name__ == "__main__":
    main()