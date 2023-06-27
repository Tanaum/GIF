from PIL import Image
import sys

images = []

for arg in sys.argv[1:]:
    img = Image.open(arg)
    images.append(img)

images[0].save(
    'face.gif', save_all = True, append_images=[images[2]], duration = 200, loop = 0
)