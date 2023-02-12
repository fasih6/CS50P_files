def main():
    a, b = frac()
    c = (float(a) / float(b)) * 100
    c = round(c)
    if c <= 1:
        print("E")
    elif c >= 99:
        print("F")
    else:
        print(f"{c}%", end="")


def frac():
    while True:
        try:
            x = (input("Fraction: "))
            y, z = x.split("/")
            y = int(y)
            z = int(z)
            if y > z:
                continue
        except:
            pass
        else:
            if z == 0:
                pass
            else:
                return y, z

main()