from sys import argv
import requests

x = 0.0

if len(argv) == 2: # len(argv) == 2 means 0,1
    try:
        x = float(argv[1])
    except:
        exit("Command-line argument is not a number")
else:
    exit("Missing command-line argument")

response = ""
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass

res = response.json()
price = res["bpi"]["USD"]["rate"]
v, y = price.split(",")
w, z = y.split(".")

priceplus = float(v + w + z) / 10000
priceplus *= x
print(f"${priceplus:,.4f}")