z = 50

while z > 0:
    print("Amount Due: ", z)
    x = int(input("Insert Coin: "))
    if x == 25 or x == 10 or x == 5:
        z = z-x
    else:
        z = 50

print("Change Owed: ",abs(z))