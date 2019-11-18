# the goal of this program is to combine all logs into one log file
import os

originalPath = r"/home/luke/Documents/logbook"
saveLocation = r"/home/luke/Documents"
outputFileLocation = "/home/luke/Documents" + "/output.txt"
open(outputFileLocation, 'w').close()
os.chdir(originalPath)

#print(originalPath)

#This entire section is way too complex. It's way too hard to code and will be even harder to debug
yearFolders = os.listdir(originalPath)
#print(yearFolders)
#Sort in Ascending numeric order
yearFolders.sort()
#print(yearFolders)
i = 0
while i < len(yearFolders): #while the count is less than number of year folders, enter year folder #n, then add one to count
    print("Entering year folder: " + yearFolders[i])
    yearFolderPath = originalPath + "/" + yearFolders[i]
    monthFolders = os.listdir(yearFolderPath)
    monthFolders.sort()
    #print(monthFolders)
    j = 0
    while j < len(monthFolders):
        print("Entering month folder: " + monthFolders[j])
        monthFolderPath = yearFolderPath + "/" + monthFolders[j]
        dateFolders = os.listdir(monthFolderPath)
        dateFolders.sort()
        #print(dateFolders)
        k = 0
        while k < len(dateFolders):
            print("Entering date folder: " + dateFolders[k])
            dateFolderPath = monthFolderPath + "/" + dateFolders[k]
            entries = os.listdir(dateFolderPath)
            entries.sort()
            #print(entries)
            d = 0
            while d < len(entries):
                print("Entering entry file: " + entries[d])
                entryPath = dateFolderPath + "/" + entries[d]
                #writes content from entry to output.txt
                with open(entryPath) as f:
                    lines = f.readlines()
                    lines = [l for l in lines]
                    #print(lines)
                    with open(outputFileLocation, "a") as f1:
                        f1.writelines(lines)
                        f1.writelines("\n")
                #open entry, copy data and save to big text file
                d = d + 1
            k = k + 1
        j = j + 1
    i = i + 1


#start from the logbook folder
    #open year folder with lowest number
        #open month folder with lowest number
            #open date folder with lowest number
                #open text file with lowest number and copy text to a new document
                #open text file with next lowest number and repeat until there are no files left
                #maybe you can store the first numbers in the name of the log that occur before the "_" and save it to a list. Then go through this list and search for the text file that is next lowest
            #open date folder with next lowest number and repeat


#output format
#year


#month year

#day month year
#time-"entry content"
