from PIL import Image, ExifTags
import glob, os, random

def rename(dir, pattern):
    files = glob.glob(os.path.join(dir, pattern))

    for pathAndFilename in files:
        try:
            image=Image.open(pathAndFilename)
            if hasattr(image, '_getexif'): # only present in JPEGs
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation]=='Orientation':
                        break
                e = image._getexif()       # returns None if no EXIF data
                if e is not None:
                    exif=dict(e.items())
                    orientation = exif[orientation]

                    if orientation == 3:   image = image.transpose(Image.ROTATE_180)
                    elif orientation == 6: image = image.transpose(Image.ROTATE_270)
                    elif orientation == 8: image = image.transpose(Image.ROTATE_90)

            image.thumbnail((240, 180), Image.ANTIALIAS)
            image.save(pathAndFilename)

        except:
            traceback.print_exc()

rename(r'../imageset_3', r'*.jpg')
