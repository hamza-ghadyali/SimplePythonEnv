# old version
# import gzip
# import sys

# opener = gzip.open

# if __name__ == "__main__":
#     f = gzip.open(sys.argv[1], mode="wt")
#     f.write(" ".join(sys.argv[2:]))
#     f.close()

# new version after creating demo_reader.util module with writer.py

import gzip
#from demo_reader.util import writer
from ..util import writer # using relative import instead

opener = gzip.open

if __name__ == "__main__":
    writer.main(opener)


