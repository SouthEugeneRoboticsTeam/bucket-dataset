from PIL import Image
import glob, os, random

def rename(dir, pattern):
    files = glob.glob(os.path.join(dir, pattern))

    for pathAndFilename in files:
        im = Image.open(pathAndFilename)
        imResize = im.resize((240,180), Image.ANTIALIAS)
        imResize.save(pathAndFilename, 'JPEG', quality=90)

rename(r'../images', r'*')
