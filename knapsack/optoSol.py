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
    numOfRuns = 10000
    startingTemp = 1000000.0
    alpha = 0.99

    # take all in sack initially
    initialGuess = np.ones(N, dtype=np.int64)
    sackAll = runAnnealing(N, rnd, fileData[2], maxWeight, numOfRuns, startingTemp, alpha, initialGuess)

    # this was going to check 3 different state states, but take all appears to do best most of the time 

                # take nothing from sack initially
                #initialGuess = np.zeros(N, dtype=np.int64)
                #sackNone = runAnnealing(N, rnd, fileData[2], maxWeight, numOfRuns, startingTemp, alpha, initialGuess)

                # random start state of sack
                #np.random.seed(RANDOM_SEED_VALUE); initialGuess = np.random.randint(2, size=N, dtype=np.int64)
                #sackRand = runAnnealing(N, rnd, fileData[2], maxWeight, numOfRuns, startingTemp, alpha, initialGuess)
    
                #(sackAllValue, sackAllWeight) = getTotalValueAndSize(sackAll, fileData[2], N)
                #(sackNoneValue, sackNoneWeight) = getTotalValueAndSize(sackNone, fileData[2], N)
                #(sackRandValue, sackRandWeight) = getTotalValueAndSize(sackRand, fileData[2], N)

                # check which stating state gives best solution
                #if( (sackAllValue >= sackNoneValue) and (sackAllValue >= sackRandValue) and (sackAllWeight <= maxWeight)):
                #    sack = sackAll
                #    print("Intial take all is best")
                #elif( (sackNoneValue >= sackRandValue) and (sackNoneWeight <= maxWeight)):
                #    sack = sackNone
                #    print("Initial take none is best")
                #elif(sackRandWeight <= maxWeight):
                #    sack = sackRand
                #    print("Initial rand state is best")
                #else:
                #    sack = sackAll
    

    # return best outcome
    return (fileData[1], constructList(sackAll, fileData[2], fileData[0]))
