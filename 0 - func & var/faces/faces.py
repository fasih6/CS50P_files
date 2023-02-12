def main():
    name = input("enter text: ")
    print(convert(name))


def convert(name):
    x = name.replace(":)", "🙂").replace(":(", "🙁")
    return x

main()