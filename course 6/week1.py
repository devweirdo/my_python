import os
from PIL import Image

yourpath = os.getcwd()
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        outfile = os.path.join(r'/opt/icons', name)
        try:
            im = Image.open(os.path.join(root, name))
            rgb_im = im.convert('RGB')
            print ("Generating jpeg for %s" % name)
            rgb_im.thumbnail(rgb_im.size)
            rgb_im.resize((128,128)).rotate(90).save(outfile, "JPEG", quality=100)
        except (OSError):
            pass