#!/usr/bin/python
import os, sys

if len(sys.argv) < 2:
    print """usage: sloc <dir>
    where <dir> is a root dir of java files you wish to analyse recursively."""
    sys.exit(0)

def average(numList):
    sum = 0
    for num in numList:
        sum += num
    return float(sum) / len(numList)

sloc = 0
numJavaFiles = 0
commentLines = 0
semicolons = 0
shortLines = 0
emptyLines = 0
lineLengths = []
linesPerFile = []
slocPerFile = []
#recursively counts significant lines of code in all java files from a given directory down
for cwd, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        if f[-4:] == 'java':
            numJavaFiles += 1
            openfile = open(os.path.join(cwd,f), 'r')
            commentsMode = False
            linesInFile = 0
            slocInFile = 0
            for line in openfile.readlines():
                linesInFile += 1
                #print line[:-1]
                semicolons += line.count(';')
                if '/*' in line:##if this line has a multiline comment, don't count sloc until the closing comment
                    commentsMode = True
                lineLen = len(line[:-1].lstrip('\t '))#the line minus the newline char at the end
                if lineLen == 0:
                    emptyLines += 1
                elif lineLen == 1:
                    shortLines += 1
                elif not commentsMode:
                    sloc += 1
                    slocInFile += 1
                    lineLengths.append(lineLen)
                elif commentsMode:
                    commentLines += 1
                if '*/' in line:
                    commentsMode = False
                if line[:2] == '//':
                    commentLines += 1
                    sloc -= 1
                    slocInFile -= 1
            openfile.close()
            linesPerFile.append(linesInFile)
            slocPerFile.append(slocInFile)

print 'significant lines of code:', sloc
print 'number of comment/doc lines:', commentLines
print 'short lines:', shortLines
print 'empty lines:', emptyLines
print 'number of java files:', numJavaFiles
print 'max significant line length:', max(lineLengths)
print 'min significant line length:', min(lineLengths)
print 'average significant line length:', average(lineLengths)
print 'max SLOC in a file:', max(slocPerFile)
print 'min SLOC in a file:', min(slocPerFile)
print 'average SLOC per file:', average(slocPerFile)
print 'semicolons used:', semicolons


