def main():
    x = input("Input: ")
    print(shorten(x))

def shorten(word):
        for i in "aeiouAEIOU":
            word= word.replace(i,"")
        return word

if __name__ == "__main__":
    main()