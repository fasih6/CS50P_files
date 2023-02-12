from PIL import Image
import PIL

from sys import argv

if len(argv) > 3:
    exit("Too many command-line arguments")
elif len(argv) < 3:
    exit("Too few command-line arguments")
else:
    y, z = argv[1].split(".")
    if z not in ['jpg', 'jpeg', 'png']:
        exit("Invalid input")
    w, x = argv[2].split(".")
    if z != x:
        exit("Input and output have different extensions")
    if x not in ["jpg","jpeg","png"]:
        exit("Invalid output")
    if z not in ["jpg","jpeg","png"]:
        exit("Invalid input")
##################################################################3
images= []
shirt = Image.open("shirt.png")
try:
    inp = Image.open(argv[1])
except:
    exit("Input does not exist")
# print(shirt.size)
# print(inp.size)
images.append(shirt)
images.append(inp)

x = PIL.ImageOps.fit(inp, (600,600), bleed=0.0, centering=(0.5, 0.5))
# shirt.paste(x,(0,100))
# shirt.save('paste.jpg')
x.paste(shirt,shirt)
x.save(argv[2])