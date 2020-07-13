#ohamilton79
#Merge sort
#02/07/2020

#Merge two sorted lists into a single sorted list
def merge(listA, listB):
    #List into which the two lists will be combined
    sortedList = []

    #Compare the intial items of list a and list b, and move the smallest value into the sorted list
    while listA != [] and listB != []:
        #Compare the heads of each list
        if listA[0] < listB[0]:
            #Append the item to the sorted list popped from the first position of list A
            sortedList.append(listA.pop(0))

        else:
            #Append the item at the first position of list B to the sorted list
            sortedList.append(listB.pop(0))

    #If list A is empty, add the reamining values in list B to the end of the sorted list
    if len(listA) < 1:
        sortedList += listB

    #Otherwise, the values in list A should be appended
    else:
        sortedList += listA

    #Return the sorted list
    return sortedList

#Carry out the merge sort
def mergeSort(unsorted):
    #If the list contains only 1 or fewer items, it can be returned
    if len(unsorted) <= 1:
        return unsorted
    #Otherwise, split the list into 2 smaller lists
    else:
        #Rounds down if an odd number of items
        middlePointer = len(unsorted) // 2
        #Create the two lists and assign them to the returned value of the mergeSort function
        front = mergeSort(unsorted[:middlePointer])
        back = mergeSort(unsorted[middlePointer:])
    #Return the two front and back lists merged together
    return merge(front, back)
