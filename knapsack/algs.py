import fileReader as fr

# grabs values until weight is over given value or there are no values remaining in list
def grabAsMuchAsPossible(limit, values):
    weight = 0
    whatToTake = []

    for row in values:
        if(int(weight) + int(row[1]) <= int(limit)):
            weight += int(row[1])
            whatToTake.append(row)

    return whatToTake

###############
# Greedy Algs #
###############

# greedy alg by sorting from least to greatest weight
def greedyByWeight(fileName):
    fileData = fr.readFile(fileName)
    fileData[2].sort(key=lambda a: a[1])

    answer = grabAsMuchAsPossible(fileData[1], fileData[2])
    return(fileData[1], answer)


# greedy alg by sorting from greatest to least value
def greedyByValue(fileName):
    fileData = fr.readFile(fileName)
    fileData[2].sort(key=lambda a: a[2], reverse=True)

    answer = grabAsMuchAsPossible(fileData[1], fileData[2])
    return(fileData[1], answer)

# greedy alg by sorting from highest (value / weight) ratio
def greedyByRatio(fileName):
    fileData = fr.readFile(fileName)
    fileData[2].sort(key=lambda a: int(a[2])/int(a[1]), reverse=True)
    
    answer = grabAsMuchAsPossible(fileData[1], fileData[2])
    return(fileData[1], answer)


###################
# exhaustive algs #
###################

# calc the value of 2 arrays and return the larger
def maxArr(listA, listB):
    aValue = 0
    bValue = 0
    for row in listA:
        aValue += row[2]
    for row in listB:
        bValue += row[2]

    if(aValue > bValue):
        return listA
    else:
        return listB

def exPruneRun(remainingWeight, n, values):
    # Base Case and prune by weight
    if (n == 0 or remainingWeight == 0):
        return []
    # can you not add the current item? Don't
    if (remainingWeight - values[n - 1][1] < 0):
       
        return exPruneRun(remainingWeight, n - 1, values)

     # try with adding and not adding
    else:
        return maxArr([values[n-1]] + exPruneRun(remainingWeight - values[n-1][1], n - 1, values), 
                                      exPruneRun(remainingWeight, n - 1, values))

# exhaustive method with prune for knapsack
def exhaustivePrune(fileName):
    fileData = fr.readFile(fileName)
    return (fileData[1], exPruneRun(fileData[1], fileData[0], fileData[2]))


# calc the value of 2 arrays and return the larger
def maxArrWithWeight(remainingWeightA, listA, remainingWeightB, listB):
    aValue = 0
    bValue = 0

    for row in listA:
        aValue += row[2]
    for row in listB:
        bValue += row[2]

    if (aValue > bValue and remainingWeightA >= 0):
        return listA
    elif (remainingWeightB >= 0):
        return listB
    else:
        return listA

def exRun(remainingWeight, n, values):
    newWeight = remainingWeight - values[n-1][1]
    # Base Case
    if (n == 0):
        return [] 

    # try with adding and not adding
    else:
       return maxArrWithWeight(newWeight, [values[n-1]] + exRun(newWeight, n - 1, values), # take selection
                                     remainingWeight, exRun(remainingWeight, n - 1, values)) # don't take selection
# exhaustive method for knapsack
def exhaustiveSearch(fileName):
    fileData = fr.readFile(fileName)
    return (fileData[1], exPruneRun(fileData[1], fileData[0], fileData[2]))

