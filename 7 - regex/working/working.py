import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        x1, y1 = s.split("to")
        x1 = x1.strip()
        y1 = y1.strip()
        t1, c = x1.split(" ")
        t2, d = y1.split(" ")

        if c == "AM" and d == "PM":
            try:
                x, y = t2.split(":")
                w, z = t1.split(":")
                if w == "12":
                    return f"00:00 to {t2}"
                x = int(x) + 12
                if int(w) < 10:
                    return f"0{t1} to {x}:{y}"
                return f"{t1} to {x}:{y}"
            except:
                if t1 == "12":
                    return f"00:00 to {t2}:00"
                t2 = int(t2) + 12
                if int(t1) < 10:
                    return f"0{t1}:00 to {t2}:00"
                return f"{t1}:00 to {t2}:00"
        if c == "PM" and d == "AM":
            try:
                x, y = t1.split(":")
                x = int(x) + 12
                w, z = t2.split(":")
                if int(w) < 10:
                    return f"{x}:{y} to 0{t2}"
                return f"{x}:{y} to {t2}"
            except:
                t1 = int(t1) + 12
                if int(t2) < 10:
                    return f"{t1}:00 to 0{t2}:00"
                return f"{t1}:00 to {t2}:00"
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()