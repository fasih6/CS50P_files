from collections import OrderedDict
d = {}

while True:
    try:
        x = input("").upper()
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    except EOFError:
        print("", end="")
        break

d = OrderedDict(sorted(d.items()))
for item in d:
    print(d[item], item)
