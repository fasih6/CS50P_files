x = ""
y = ""
z = ""
d = {
    "January": "1",
    "February":"2",
    "March":"3",
    "April":"4",
    "May":"5",
    "June":"6",
    "July":"7",
    "August":"8",
    "September":"9",
    "October":"10",
    "November":"11",
    "December":"12"
}
while True:
    a = input("Date: ").strip()
    try:
        x,y,z = a.split("/") # x = month, y = day, z = year
        if int(x) > 12 or int(y) > 31:
            continue
        break
    except:
        if a[-6] != ",":
            continue
        x,y,z = a.split()
        y = y.strip(", ")
        # error  -->   8 September 1636
        # accep  -->   September 8, 1636
        if len(y) > 2 or int(y) > 31:
            continue
        if x in d:
            x = d[x]
            break

if 1 < int(x) < 10:
    x = "0"+x
if 1 < int(y) < 10:
    y = "0"+y
print(f"{z}-{x}-{y}")