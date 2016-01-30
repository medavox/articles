#!/usr/bin/python
#python 2
import os, math, sys

#now runs on all .cti files in its directory, if given no arguments!

freqOut = open(os.path.join(os.getcwd(),"allFreqs.csv"), 'wb')
magOut = open(os.path.join(os.getcwd(),"allMags.csv"), 'wb')
logMagOut = open(os.path.join(os.getcwd(),"allLogMags.csv"), 'wb')
phaseOut = open(os.path.join(os.getcwd(),"allPhases.csv"), 'wb')

def convertToCSV(fileInput):
    openfile = open(os.path.join(os.getcwd(),fileInput), 'rb')
    inputLines = openfile.readlines()
    i = 0
    #remove carriage return characters from the end of each line
    while i < len(inputLines):
        inputLines[i] = inputLines[i].rstrip("\r\n")
        i += 1
    #freqs = allTheLinesInTheFile[3:4000]
    freqs = inputLines[inputLines.index("VAR_LIST_BEGIN")+1:inputLines.index("VAR_LIST_END")]
    magsnphases = inputLines[inputLines.index("BEGIN")+1:inputLines.index("END")]

    magnitudes = []#have to define these as empty arrays before I can append to them
    phases = []
    
    #Split the magnitudes and phases 
    for line in magsnphases:
        anb = line.split(",")
        magnitudes.append(anb[0])
        phases.append(anb[1])
    
    #create a column of 20(log10 phase)
    logMags = [20 * math.log(float(x), 10) for x in magnitudes]

    #check to make sure there are the same number of rows for each data column
    if not ( len(magnitudes) == len(freqs) == len(phases) == len(logMags)):
        print "ERROR! Number of data points for all columns do not match! Exiting."
        sys.exit(1)
    #dynamically generate output filename from input
    fileOutput = fileInput.replace(".cti",".csv")#use redundant search term to ensure i don't replace the wrong text
    owtpwt = open(os.path.join(os.getcwd(),fileOutput), 'wb')
    s = ","
    owtpwt.write("frequency / Hz,Magnitude / mV,20log10(Magnitude) / dB,Phase / degrees\n")
    j = 0
    while j < len(freqs):
        #write a line to the main output file
        owtpwt.write(freqs[j] + s + magnitudes[j] + s + str(logMags[j]) + s + phases[j] + "\n")
        #write relevant columns to a file which accumulates the results of multiple CTIs
        freqOut.write(freqs[j] + s)
        magOut.write(magnitudes[j] + s)
        logMagOut.write(str(logMags[j]) + s)
        phaseOut.write(phases[j] + s)
        j += 1#mustn't forget to increment
    
    owtpwt.close()
    openfile.close()
    print "wrote", len(freqs), "rows to", fileOutput
    #---------------------------------------------------------------------------
#run the main cti2csv function on all cti files passed as arguments
args = []
if len(sys.argv) <= 1:
    for f in os.listdir("."):
        if f[-4:] == '.cti':
            args.append(f)
else:
    args = sys.argv[1:]
for ffael in args:#it spells file in welsh phonetics
    convertToCSV(ffael)
    freqOut.write("\n")
    magOut.write("\n")
    logMagOut.write("\n")
    phaseOut.write("\n")

freqOut.close()
magOut.close()
logMagOut.close()
phaseOut.close()

#generate averages from the allXs.csv files
def average(filename):
    fileopened = open(os.path.join(os.getcwd(), filename), 'rb')
    dataMatrix = []
    avgs = []
    maxs = []
    mins = []
    print "beginning averages for file", filename
    #build data matrix: columns are data points in a run, rows are different runs
    for line in fileopened.readlines():
        dataMatrix.append(line.split(","))
    
    h = 0
    while h < len(dataMatrix):
        dataMatrix[h] = dataMatrix[h][:-1]#remove empty last elements
        h += 1
    
    col = 0
    print "\tdatamatrix:", len(dataMatrix), "by", len(dataMatrix[0])
    print "\t(should be >1 by 20,001, or number of results)"
    while col < len(dataMatrix[0]):
        sum = 0
        row = 0
        
        vals = [dataMatrix[x][col] for x in range(0, len(dataMatrix)) ]
        maxs.append(max(vals))
        mins.append(min(vals))
        
        while row < len(dataMatrix):
            #print "adding dataMatrix[", row,"][", col, "] to sum (=", sum
            #work out maxs and mins            
            sum += float(dataMatrix[row][col])
            row += 1
        avg = sum / len(dataMatrix)
        avgs.append(avg)
        col += 1
    print "\twriting averages to", filename.replace("all","avg")
    print "\twriting max vals to", filename.replace("all","avg")
    print "\twriting min vals to", filename.replace("all","avg")
    avgOut = open(os.path.join(os.getcwd(), filename.replace("all","avg")), 'wb')
    maxOut = open(os.path.join(os.getcwd(), filename.replace("all","max")), 'wb')
    minOut = open(os.path.join(os.getcwd(), filename.replace("all","min")), 'wb')
    for e in avgs:
        avgOut.write(str(e)+"\n")
    for e in maxs:
        maxOut.write(str(e)+"\n")
    for e in mins:
        minOut.write(str(e)+"\n")
    fileopened.close()
    avgOut.close()
    maxOut.close()
    minOut.close()
    #----------------------------------------------

average("allFreqs.csv")
average("allMags.csv")
average("allLogMags.csv")
average("allPhases.csv")

print "removing allX.csv files"
os.remove("allFreqs.csv")
os.remove("allMags.csv")
os.remove("allLogMags.csv")
os.remove("allPhases.csv")
#TODO
#Save the values of the lowest and highest freqs / magnitudes / logMags / phases
#Plot out on graphs? Avfreqs(x) [should be the same as the normal values] vs Avmagnitudes / Av logMags / Avphases
