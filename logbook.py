#You should make a program that compiles all of the log files into one big file that you can read all at once or several smaller ones for each month or year

# import the os module
import os #makes directory modification work
from datetime import datetime #gets date and time
import webbrowser

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

originalPath = "/home/luke/Documents"
os.chdir(originalPath) #eventually you should make this part change
#the directory to a patht that the user chooses, after that path has been chosen
#the path will be stored in a text file beside the logbook.py program which
#will tell the prgram where to put the log files at.
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
logNumOfTheDay = 1
datePartOfLogname = now.strftime("%m-%d-%Y")
logname = str(logNumOfTheDay) + "_" + datePartOfLogname
finalLogPath = datePath + "/" + logname
while (os.path.exists(finalLogPath)):
    logNumOfTheDay = logNumOfTheDay + 1
    logname = str(logNumOfTheDay) + "_" + datePartOfLogname
    finalLogPath = datePath + "/" + logname
print(logname)

finalLogPath = datePath + "/" + logname
f = open(finalLogPath,"w+")

#writes date and time as first line of txt file
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
f.write(dt_string)

webbrowser.open(finalLogPath) #opens txt file in text editor
