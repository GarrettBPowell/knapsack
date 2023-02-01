import csv
import os

# reads data in from file and returns a tuple that is
# Number of Items, Max Weight, List of data points
# data points are a touple of (label, weight, value)

def readFile():
    NumItems = -1 
    MaxWeight = -1
    pairedValues = []

    print("What is the name of the file in the cases folder that you want to use? (No extension)")

    user_input = input()
    fileName = os.path.abspath('resources/' + user_input + '.csv')

    with open(fileName) as openFile:
        csvReader = csv.reader(openFile, delimiter=',')

        lineNum = 0
        for row in csvReader:
            if(lineNum == 0):
                NumItems, MaxWeight = row #save values

                MaxWeight = int(MaxWeight.replace(' ', '')) #remove that stupid space and convert to int
                NumItems = int(NumItems) #convert to int

                lineNum += 1
            elif(lineNum != 0):
                pairedValues.append(row)

    return (NumItems, MaxWeight, pairedValues)

def grabAsMuchAsPossible(limit, values):
    weight = 0
    whatToTake = []

    for row in values:
        if(int(weight) + int(row[1]) <= int(limit)):
            weight += int(row[1])
            whatToTake.append(row)

    return whatToTake





def greedyByWeight():
    fileData = readFile()
    fileData[2].sort(key=lambda a: a[1])

    answer = grabAsMuchAsPossible(fileData[1], fileData[2])
    return(fileData[1], answer)

def greedyByValue():
    fileData = readFile()
    fileData[2].sort(key=lambda a: a[2], reverse=True)

    answer = grabAsMuchAsPossible(fileData[1], fileData[2])
    return(fileData[1], answer)

def greedyByRatio():
    fileData = readFile()
    fileData[2].sort(key=lambda a: int(a[2])/int(a[1]), reverse=True)
    
    answer = grabAsMuchAsPossible(fileData[1], fileData[2])
    return(fileData[1], answer)