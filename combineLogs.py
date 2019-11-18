# the goal of this program is to combine all logs into one log file
i = 0
j = 0
k = 0
d = 0
import os
import glob

originalPath = r"/home/luke/Documents/logbook"
os.chdir(originalPath)
#print(originalPath)


yearFolders = os.listdir(originalPath)
#print(yearFolders)
#Sort in Ascending numeric order
yearFolders.sort()
#print(yearFolders)
while i < len(yearFolders):
    print("Entering folder: " + yearFolders[i])
    yearFolderPath = originalPath + "/" + yearFolders[i]
    monthFolders = os.listdir(yearFolderPath)
    monthFolders.sort()
    #print(monthFolders)
    while j < len(monthFolders):
        print("Entering folder: " + monthFolders[j])
        monthFolderPath = yearFolderPath + "/" + monthFolders[j]
        dateFolders = os.listdir(monthFolderPath)
        dateFolders.sort()
        #print(dateFolders)
        while k < len(dateFolders):
            print("Entering folder: " + dateFolders[k])
            dateFolderPath = monthFolderPath + "/" + dateFolders[k]
            entries = os.listdir(dateFolderPath)
            entries.sort()
            print(entries)
            while d < len(entries):
                print("Entering file: " + entries[d])
                entryPath = dateFolderPath + "/" + entries[d]
                #open entry, copy data and save to big text file
                d = d + 1
            k = k + 1
        j = j + 1
    i = i + 1

#while the count is less than number of year folders, enter year folder #n, then add one to count

#start from the logbook folder
    #open year folder with lowest number
        #open month folder with lowest number
            #open date folder with lowest number
                #open text file with lowest number and copy text to a new document
                #open text file with next lowest number and repeat until there are no files left
                #maybe you can store the first numbers in the name of the log that occur before the "_" and save it to a list. Then go through this list and search for the text file that is next lowest
            #open date folder with next lowest number and repeat
