#ohamilton79
#Bubble sort
#01/07/2020

#Function for bubble sort
def bubbleSort(unsortedList):
    #Make a copy of the list, leaving the original untouched
    sortedList = unsortedList[:]

    #Initialise a swapped variable with the value True
    swapped = True

    #Run while swapped is true
    while swapped:
        #Set swapped to false before making comparisons for this pass
        swapped = False

        #Iterate over the sorted list
        for i in range(len(sortedList)-1):
            #If the first item is greater than the next
            if sortedList[i] > sortedList[i + 1]:
                #Swap them
                sortedList[i], sortedList[i+1] = sortedList[i+1], sortedList[i]

                #Set the swapped flag to True
                swapped = True

    #Once no swaps have been made for a full pass, return the sorted list
    return sortedList
