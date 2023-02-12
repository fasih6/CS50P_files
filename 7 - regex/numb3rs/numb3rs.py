import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    


def validate(ip):
    try:
        w,x,y,z = ip.split(".")
        if 0 <= int(w) <= 255 and 0 <= int(x) <= 255 and 0 <= int(y) <= 255 and 0 <= int(z) <= 255:
            return True
        else:
            return False
    except:
        return False




if __name__ == "__main__":
    main()