import fileReader as fr
import numpy as np

# randomly flips an item in the sack 
def adjacent(sack, rnd, n):
    # make new binary array to change
    result = np.copy(sack)

    # pick a random index to flip
    i = rnd.randint(n)

    if result[i] == 0:
        result[i] = 1
    elif result[i] == 1:
        result[i] = 0

    return result

# returns the value and size of items taken in sack
def getTotalValueAndSize(sack, data, maxSize):

  totalVal = 0  # total value of items selected in sack
  totalSize = 0  # total weight of items selected in sack

  # Count up value and weight
  i = 0;
  for row in data:
    if sack[i] == 1:
        totalVal += row[2]
        totalSize += row[1]
    i+=1

  #print(totalSize, maxSize, totalVal)

  # if weight exceeds the maxSize, set value to 0
  if totalSize > maxSize: 
    totalVal = 0

  return (totalVal, totalSize)

def runAnnealing(n, rnd, data, maxWeight, numOfRuns, startingTemp, alpha, currentSack):
    # save temp to modify
    currentTemp = startingTemp

    # set starting values
    iteration = 0
    interval = np.round(numOfRuns, -1)

    (currentVal, curr_size) = getTotalValueAndSize(currentSack, data, maxWeight)

    while( iteration < numOfRuns):
        adjustedSack = adjacent(currentSack, rnd, n)
        (newSackVal, _) = getTotalValueAndSize(adjustedSack, data, maxWeight)

        # The new value is better so take it instead
        if newSackVal > currentVal:  
            currentSack = adjustedSack
            currentVal = newSackVal

        # Don't take the new value (unless you randomly do)
        else:        
            # calculate probability of take anyway based off of this formula
            # https://www.researchgate.net/publication/227061666_Computing_the_Initial_Temperature_of_Simulated_Annealing#:~:text=The%20classical%20version%20of%20simulated,with%20a%20given%20acceptance%20ratio.
            # metroplois acceptance criterion 
            probAccept = np.exp((newSackVal - currentVal) / currentTemp) 
        
            # get rand probability to take or not
            p = rnd.random()

            # take option near current solution anyway
            if p < probAccept: 
                currentSack = adjustedSack
                currentVal = newSackVal 

        # keep temp at a resonable decimal 
        if( currentTemp < 0.00001):
            currentTemp = 0.00001
        else:
            currentTemp *= alpha

        # increment 
        iteration += 1

    return currentSack             

# turns binary list into taken items from data that can be printed
def constructList(sack, data, n):
    returnList = []
    for i in range(n):
        if( sack[i] == 1):
            returnList += [data[i]]

    return returnList


def annealing(fileName):
    RANDOM_SEED_VALUE= 5
    fileData = fr.readFile(fileName)

    N = fileData[0]
    maxWeight = fileData[1]

    # non seeded rand
    rnd = np.random.RandomState(RANDOM_SEED_VALUE) 
    numOfRuns = 1000
    startingTemp = 10000.0
    alpha = 0.99

    # take all in sack initially
    valueOfCurrentSack = 0;
    initialGuess = np.ones(N, dtype=np.int64)
    takeThisSack = np.ones(N, dtype=np.int64) # the final sack we take
    i = 0
    while(valueOfCurrentSack == 0 or i < 10):
        sackAll = runAnnealing(N, rnd, fileData[2], maxWeight, numOfRuns, startingTemp, alpha, initialGuess)

        # calc values of sack options
        valueOfCurrentSack = getTotalValueAndSize(sackAll, fileData[2], maxWeight)[0]
        valueOfTakeSack = getTotalValueAndSize(takeThisSack, fileData[2], maxWeight)[0]
        # compare values
        if(valueOfCurrentSack > valueOfTakeSack):
            takeThisSack = sackAll
        #print(sackAll)
        initialGuess = sackAll # if the check fails start with last best guess 
        i += 1   

    # return best outcome
    return (fileData[1], constructList(takeThisSack, fileData[2], fileData[0]))
