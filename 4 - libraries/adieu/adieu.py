import sys

l = []

while True:
    try:
        x = input("Name: ")
        if x:
            l.append(x)
        # else:
        #     break
    except EOFError:
        print("")
        break


if len(l) == 1:
    print(f"Adieu, adieu, to {l[0]}")
    exit()
elif len(l) == 2:
    print(f"Adieu, adieu, to {l[0]} and {l[1]}")
    exit()

w = "Adieu, adieu, to"

for i in range(len(l)-1):
    w += " "
    w += l[i] + ","

print(w+" and "+l[-1])
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl