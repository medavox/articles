#!/usr/bin/python
import os, sys
ignoreCase = False
exactMatch = False
for arg in sys.argv:
    if arg == "-i":
        ignoreCase = True
    if arg == "-e":
        exactMatch = True

if len(sys.argv) < 2:
    print "usage:" + sys.argv[0] +  """<opts> file
    Searches for a file recursively.
    
    -i  ignore case"""
    sys.exit(0)
matches = 0
#recursively walks a file tree, from a given directory down
for cwd, dirs, files in os.walk("."):
    for f in files:
        match = False
        if ignoreCase:
            if sys.argv[-1].lower() in f.lower():
                match = True            
        else:
            if sys.argv[-1] in f:
                match = True
        if match:
            match = False
            matches += 1
            print(os.path.join(cwd,f))

