def main():
    x = input("what time is it? ")
    y = convert(x)
    if 7 <= y <= 8:
        print("breakfast time")
    elif 12 <= y <= 13:
        print("lunch time")
    elif 18 <= y <= 19:
    	print("dinner time")



def convert(time):
	h, m = time.split(":")
	h = int(h)
	m = float(m)
	m = m / 60
	m = round(m, 2)
	return h + m



if __name__ == "__main__":
    main()