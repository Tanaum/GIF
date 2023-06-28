from PIL import Image
import sys

images = []

for arg in sys.argv[1:]:
    img = Image.open(arg)
    images.append(img)

i = 0
while i != 1:
    images[i].save(
        'face.gif', save_all = True, append_images=[images[1+1]], duration = 200, loop = 0
    )
    i+=1
