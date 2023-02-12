def main():
    x = (input("Fraction: "))
    c = convert(x)
    if c or c==0:
        print(gauge(c))

def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"

def convert(fraction):
    while True:
        try:
            y, z = fraction.split("/")
            y = int(y)
            z = int(z)
            if z == 0:
                raise ZeroDivisionError
            if y > z:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            return round((float(y) / float(z)) * 100)

if __name__ == "__main__":
    main()