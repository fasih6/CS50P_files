txt = input("enter: ")

x, y, z = txt.split()
x = float(x)
z = float(z)


match y:
    case "+":
        print(f"{x + z:.1f}")
    case "/":
        print(f"{x / z:.1f}")
    case "-":
        print(f"{x - z:.1f}")
    case "*":
        print(f"{x * z:.1f}")
