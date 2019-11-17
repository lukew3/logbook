# the goal of this program is to combine all logs into one log file

import os
import glob

originalPath = "/home/luke/Documents/logbook"
os.chdir(originalPath)
#print(originalPath)

#for file in glob.glob("*.txt"):
#    print(file)

spath = r"/home/luke/Documents/logbook"
#os.walk is the way to go, I just don't know how to use it
#for root, dirs, files in os.walk(originalPath):
#    for f in files:
#        fullpath = os.path.join(root, f)
#        if os.path.splitext(fullpath)[1] == '.txt':
#            print fullpath

for roots, dirs, files in os.walk(spath):
    for dir in dirs:
        print("Dir = %s" % dir)
    for file in files:
        print("File = %s" % file)

#start from the logbook folder
    #open year folder with lowest number
        #open month folder with lowest number
            #open date folder with lowest number
                #open text file with lowest number and copy text to a new document
                #open text file with next lowest number and repeat until there are no files left
                #maybe you can store the first numbers in the name of the log that occur before the "_" and save it to a list. Then go through this list and search for the text file that is next lowest
            #open date folder with next lowest number and repeat
