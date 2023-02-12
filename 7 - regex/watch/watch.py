import re
import sys

def main():
    try:
        print(parse(input("HTML: ")))
    except:
        print("None")

def parse(s):
    if s.startswith("<iframe") == 0:
        return f"None"
    try:
        matches = re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", s)
        return f"https://youtu.be/{matches.group(1)}"
    except:
        return f"None"

if __name__ == "__main__":
    main()