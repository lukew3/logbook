# the goal of this program is to combine all logs into one log file

import os
import glob

originalPath = "/home/luke/Documents/logbook"
os.chdir(originalPath)
print(originalPath)

#for file in glob.glob("*.txt"):
#    print(file)

#os.walk is the way to go, I just don't know how to use it
for root, dirs, files in os.walk(originalPath):
    for f in files:
        fullpath = os.path.join(root, f)
        if os.path.splitext(fullpath)[1] == '.txt':
            print fullpath
