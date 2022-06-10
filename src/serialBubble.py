from copy import deepcopy
import random
import time

def serialbubbleSort(array):
    '''
    Sort the list of integers through the Bubble Sort Algorithm (Serial Implementation)
    '''
    size = len(array)
    temp = deepcopy(array)
    for i in range(size):
        swap = False            #reset swap flag to false
        for j in range(size-i-1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j] #Swap list elements
                swap = True                                 #Set swap flag to true
        if not swap:       #If swap remains false, break loop
            break          #This means that the array is already sorted
    return temp

N = int(input("Enter array size: "))
unsortedArray = []
for i in range(N):
    unsortedArray.append(round(random.uniform(-N//2, N//2), 2))   #Generate randomized array

#Set timer and run function
start = time.time()
sortedArray = serialbubbleSort(unsortedArray)
end = time.time()

#print("Unsorted Array:",unsortedArray)      #Print unsorted array
#print("Sorted Array:  ",sortedArray)      #Print sorted array(output)
print("Time elapsed:", end-start)