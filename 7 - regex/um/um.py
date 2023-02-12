import re
import sys


def main():
    print(count(input("Text: ")))
    # count("um, hello, um, world")


def count(s):
    # return len(re.findall(r"\bum\b", s))
    s = s.lower()
    a = len(re.findall("um", s))
    b = len(re.findall("[abcdefghijklmnopqrstvwxyz]+um[abcdefghijklmnopqrstvwxyz]+?", s))
    c = len(re.findall("[abcdefghijklmnopqrstvwxyz]+?um[abcdefghijklmnopqrstvwxyz]+", s))
    return a-b-c


if __name__ == "__main__":
    main()