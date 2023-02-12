a = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
def main():
    total = 0
    while True:
        try:
            y = input("Item: ").title()
            if finditem(y):
                total += a[y]
                print(f"Total: ${total:.2f}")
                continue
            else:
                continue
        except EOFError:
            print("")
            break


def finditem(x):
    b = False
    for item in a:
        if item == x:
            b = True
            break
    return b

main()