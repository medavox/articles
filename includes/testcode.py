#!/usr/bin/python
import os, sys

if len(sys.argv) < 2:
    print "usage:" + sys.argv[0] +  """<dir>
    where <dir> is a root dir of files you wish to analyse recursively."""
    sys.exit(0)

#recursively walks a file tree, from a given directory down
for cwd, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        if f[-4:] == 'java':
            openfile = open(os.path.join(cwd,f), 'r')
            #add stuff here
            for line in openfile.readlines():
                pass#add stuff here
            openfile.close()

