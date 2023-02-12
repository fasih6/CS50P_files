x = input("camelCase: ")

def checklower(x):
    for i in range(len(x)):
        if x[i].isupper():
            return False
    return True

if checklower(x):
    print(x)
else:
    for i in range(len(x)):
        if x[i].isupper():
            x = x.replace(x[i], "_"+x[i].lower())
    print(x)