# import the os module
import os #makes directory modification work
from datetime import datetime #gets date and time
import webbrowser

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

originalPath = "/home/luke/Documents"
os.chdir(originalPath) #maybe allow for the user to choose save destination in the future
path = os.getcwd()
print ("The current working directory is %s" % path)


#Too much recursion in the lines below, make a function that repeats it for you
logPath = originalPath+"/logbook"

if not os.path.exists(logPath):
    os.mkdir(logPath)
    print("logbook created")
else:
    print("logbook path exists")

year = now.strftime("%Y")
yearPath = logPath + "/" + year #makes the yearPath string equal to the logpath plus the year

if not os.path.exists(yearPath):
    os.mkdir(yearPath)
    print(year + " folder created")
else:
    print(year + " path exists")

month = now.strftime("%m")
monthPath = yearPath + "/" + month

if not os.path.exists(monthPath):
    os.mkdir(monthPath)
    print(month + " folder created")
else:
    print(month + " path exists")

date = now.strftime("%d")
datePath = monthPath + "/" + date

if not os.path.exists(datePath):
    os.mkdir(datePath)
    print(date + " folder created")
else:
    print(date + " path exists")


#Makes text file
#determines what to call the text file depending on the date and how many files have been created on that date
logNumOfTheDay = 1
datePartOfLogname = now.strftime("%m-%d-%Y")
logname = str(logNumOfTheDay) + "_" + datePartOfLogname
finalLogPath = datePath + "/" + logname
while (os.path.exists(finalLogPath)):
    logNumOfTheDay = logNumOfTheDay + 1
    logname = str(logNumOfTheDay) + "_" + datePartOfLogname
    finalLogPath = datePath + "/" + logname

finalLogPath = datePath + "/" + logname
f = open(finalLogPath,"w+")

#writes date and time as first line of txt file
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
f.write(dt_string)
print("File saved as " + logname)
webbrowser.open(finalLogPath) #opens txt file in text editor
