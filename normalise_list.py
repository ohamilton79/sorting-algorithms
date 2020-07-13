#ohamilton79
#13/07/2020
#Convert between units

def normalise(inputList, units):
    currentUnitIndex = 0

    #If the largest time is less than 1, convert to to the next unit
    while max(inputList) < 1:
        currentUnitIndex += 1
        #Convert the times to the new unit
        for i, item in enumerate(inputList):
            #Multiply by 10^3 (convert to the next unit)
            inputList[i] = item * 10**3

    #Return the modified input list and index of the current unit
    return inputList, currentUnitIndex

