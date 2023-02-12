def main():
    name = input("enter: ")
    print(value(name))


def value(name):
    name = name.strip().lower()
    if name.startswith("hello"):
        return f"$0"
    elif name.startswith("h"):
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()