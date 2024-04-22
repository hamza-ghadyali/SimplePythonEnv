#print("printing multi-reader-program/__main__.py")


import sys

from demo_reader.multireader import MultiReader

filename = sys.argv[1]
r = MultiReader(filename)
print(r.read())
r.close()

# run this as an executable program from the dir containing multi-reader-program
# $python multi-reader-program test.bz2

# Executable zip file
# cd multi-program
# python -m zipfile -c ../multi-reader-program.zip * 
# python multi-program-reader.zip test.bz2

# the zip file takes the place of the directory
# as such the zip file contains the contents of the dir but not the dir itself




