import os, sys, glob
from PIL import Image

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
