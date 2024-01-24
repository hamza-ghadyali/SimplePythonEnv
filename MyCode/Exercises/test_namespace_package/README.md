demo_reader module has been split with contents in path1 and path2

namespace packages allow a single logical module to be put together from multiple directories

this time it is very important that there is NOT a __init__.py file under demo_reader

if you leave the __init__.py under path1/demo_reader, then when you try to import demo_reader, it only imports the contents from path1 and not from path2.

starting a python repl from this directory (./ == test_namespace_package)
you need to add path1 and path2 to sys.path

at the repl

import sys
sys.path.extend(['./path1', './path2'])

import demo_reader
demo_reader.__path__
import demo_reader.util demo_reader.compressed
demo_reader.util.__path__
demo_reader.compressed.__path__

