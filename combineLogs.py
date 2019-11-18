# the goal of this program is to combine all logs into one log file
import os

originalPath = r"/home/luke/Documents/logbook"
saveLocation = r"/home/luke/Documents"
outputFileLocation = "/home/luke/Documents" + "/output.txt"
open(outputFileLocation, 'w').close()
os.chdir(originalPath)

#print(originalPath)

#This entire section is way too complex. It's way too hard to code and will be even harder to debug

#The code below works like this:
#a list is made that contains all the contents of a folder
#The list is then sorted so that the files that start with lower numbers are put at the front and files with higher numbers are put at the back
#The while loop then travels up the list, starting from the bottom and does the same thing for subfolders
#Once the date folder is entered, the files are read and written to output folder
yearFolders = os.listdir(originalPath)
yearFolders.sort() #Sort in Ascending numeric order
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
        k = 0
        while k < len(dateFolders):
            print("Entering date folder: " + dateFolders[k])
            dateFolderPath = monthFolderPath + "/" + dateFolders[k]
            entries = os.listdir(dateFolderPath)
            entries.sort()
            d = 0
            while d < len(entries):
                print("Entering entry file: " + entries[d])
                entryPath = dateFolderPath + "/" + entries[d]
                #writes content from entry to output.txt
                with open(entryPath) as f:
                    lines = f.readlines()
                    lines = [l for l in lines]
                    with open(outputFileLocation, "a") as f1:
                        f1.writelines(lines)
                        f1.writelines("\n")
                d = d + 1
            k = k + 1
        j = j + 1
    i = i + 1

#Sample output format
#year


#month year

#day month year
#time-"entry content"
