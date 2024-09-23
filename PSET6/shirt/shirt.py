import sys
from os.path import splitext
from PIL import Image, ImageOps

# Checks if command-line is correct
if len(sys.argv) != 3:
    sys.exit("Invalid argument number")
_, ext1 = splitext(sys.argv[1])
_, ext2 = splitext(sys.argv[2])
if ext1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid file format")
if ext1 not in sys.argv[2]:
    sys.exit("Input and output have different extensions")

# Opens and edits the images
try:
    img1 = Image.open(sys.argv[1])
    img2 = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("File not found")
size = img2.size
muppetshirt = ImageOps.fit(img1, size)
muppetshirt.paste(img2, img2)

muppetshirt.save(sys.argv[2])
