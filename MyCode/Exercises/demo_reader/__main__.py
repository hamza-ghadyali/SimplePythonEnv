# executable package experiment
print("running demo_reader/__main__.py")
import sys

from .multireader import MultiReader

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

# as an "executable package" we have demo_reader with it's own __main__.py
# so this can be executed with 
# $python -m demo_reader test.gz
# in contrast, before with "executable directory"  
# we have multi-reader-program containing __main__.py and demo_reader module
# but the demo_reader module had no __main__
# so here we execute the multi-reader program without -m flag
# $python multi-reader-program test.bz2
# and the multi-reader-program directory is being executed as a program not module


