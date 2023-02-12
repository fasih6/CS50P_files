def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s == "CS50" or s == "ECTO88" or s == "NRVOUS":
        return True
    else:
        return False


if __name__ == "__main__":
    main()