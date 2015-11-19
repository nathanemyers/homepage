import os, sys, glob
from PIL import Image

# This utility is intended for bulk resizing of images
# so we can make thumbnails and acceptably sized full size
# images.  Note that it strips EXIF data.

size = 128, 128

input_dir = sys.argv[1] + '*'
input_files = glob.glob(input_dir)
output_dir = sys.argv[2] 

for infile in input_files:
    outfile = output_dir + '/' + os.path.basename(infile)
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
