import emoji

x = input("Input: ")
try:
    a, b = x.split()
except:
    print(emoji.emojize(f'Output: {x}', language="alias"))
else:
    print(emoji.emojize(f"{a} {b}", language="alias"))

# :thumbs_up: :thumbsup: hello, :earth_africa: hello, :earth_americas: