# the goal of this program is to combine all logs into one log file
import os

originalPath = r"/home/luke/Documents/logbook"
saveLocation = r"/home/luke/Documents"
outputFileLocation = "/home/luke/Documents" + "/output.txt"

yearParameters = ["monthFolders", "yearFolderPath", "originalPath", "yearFolders", "i", "monthParameters"]
monthParameters = ["dateFolders", "monthFolderPath", "yearFolderPath", "monthFolders", "j", "dateParameters"]
dateParameters = ["entries", "dateFolderPath", "monthFolderPath", "dateFolders", "k", "none"]

def makeList(ogPath, prevList, counter):
        #print("Entering: " + prevList[counter])
        nextPath = ogPath + "/" + prevList[counter]
        newList = os.listdir(nextPath)
        newList.sort()
        return newList, nextPath

def makeFolderList(nextFolderList, currentPath, lastPath, currentFolderList, counterName, nextParamList):
    counterName = 0
    while counterName < len(currentFolderList):
        nextFolderList, currentPath = makeList(lastPath, currentFolderList, counterName)
        if nextParamList != "none":
            makeFolderList(*nextParamList)
        elif nextParamList == "none":
            addData(nextFolderList)
        counterName = counterName + 1

def addData(entries):
    d = 0
    while d < len(entries):
        #print("Entering entry file: " + entries[d])
        entryPath = dateFolderPath + "/" + entries[d]
        #writes content from entry to output.txt
        with open(entryPath) as f:
            lines = f.readlines()
            lines = [l for l in lines]
            with open(outputFileLocation, "a") as f1:
                f1.writelines(lines)
                f1.writelines("\n")
        d = d + 1

def main():

    if os.path.exists(outputFileLocation): #If file output.txt exists, remove it. If it doesn't, create it
        os.remove(outputFileLocation)
    else:
        open(outputFileLocation, 'a').close()
        print("Output.txt created")


#The code below works like this:
#a list is made that contains all the contents of a folder
#The list is then sorted so that the files that start with lower numbers are put at the front and files with higher numbers are put at the back
#The while loop then travels up the list, starting from the bottom and does the same thing for subfolders
#Once the date folder is entered, the files are read and written to output folder

    yearFolders = os.listdir(originalPath)
    yearFolders.sort() #Sort in Ascending numeric order

    makeFolderList(*yearParameters)

    print("Logs combined")

main()
#Sample output format
#year


#month year

#day month year
#time-"entry content"
