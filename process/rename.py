import glob, os, random

def rename(dir, pattern):
    i = 0

    files = glob.glob(os.path.join(dir, pattern))
    print(files)
    random.shuffle(files)

    for pathAndFilename in files:
        i+=1
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, os.path.join(dir, "%05d.jpg" % i))

rename(r'../images', r'*')
