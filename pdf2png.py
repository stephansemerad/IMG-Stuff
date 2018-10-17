from wand.image import Image
from wand.display import display

with Image(filename='atrium_bercy.pdf', resolution=300) as img:
    img.alpha_channel = False
    img.save(filename='atrium_bercy/image.png')
