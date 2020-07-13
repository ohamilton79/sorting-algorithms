#ohamilton79
#03/07/2020
#Sorting efficiency calculator

#Local libraries
from merge_sort import mergeSort
from bubble_sort import bubbleSort
from normalise_list import normalise

import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

listSize = 1000

#Generate a large random list
print("Generating list...")
listToSort = [randint(0, 1000) for i in range(listSize)]

#Create anonymous functions to use with timeit
bs = lambda: bubbleSort(listToSort)
ms = lambda: mergeSort(listToSort)
bis = lambda: sorted(listToSort)

print("Timing sorting algorithms...")
#Time the function for 100 runs each
mergeTime = timeit(ms, number = 100)

bubbleTime = timeit(bs, number = 100)

builtInTime = timeit(bis, number = 100)

#Assemble times into a list for plotting a graph
times = [mergeTime, bubbleTime, builtInTime]

#Get units for time
units = ["seconds", "milliseconds", "microseconds", "nanoseconds"]

#Normalise the times taken for each algorithm, returning the new list of times and index of the unit used in the units list
times, currentUnitIndex = normalise(times, units)

#Plot results
print("Plotting results...")
plt.bar(range(3), times, align='center', alpha=0.5)

plt.xticks(range(3), ("Merge Sort", "Bubble Sort", "Built-in Sort"))
plt.ylabel("Time taken ({})".format(units[currentUnitIndex]))
plt.xlabel("Sorting algorithm")
plt.title("Efficiency of sorting algorithms")

#Show the plot
plt.show()

