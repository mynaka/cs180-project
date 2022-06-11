from copy import deepcopy
import random
import time

def serialshellSort(array):
    '''
    Perfom shell sort of an array with length n. Initial gap is n/2.
    '''
    index = 0
    gap = len(array)//2         #initial gap is the length of the array/2

    #Perform sorting
    while gap > 0:              
        if (index + gap) < len(array):
            if(array[index] > array[index+gap]):  
                array[index], array[index+gap] = array[index+gap], array[index] #swap
            index+=1                                                            #next index
        else:                   #if index+gap is out of bounds, reset and continue to next while iteration                                                
            index = 0
            gap = gap//2
    return array
 
def printArray(unsortedArray, sortedArray):
    '''
    Print input and output arrays
    '''
    print("Unsorted Arrray:",unsortedArray)    #Print unsorted array
    print("Sorted Array:   ",sortedArray)      #Print sorted array(output)
 
N = int(input("Enter array size: "))
array = []
for i in range(N):
    array.append(round(random.uniform(-N//2, N//2), 2))   #Generate randomized array
unsortedArray = deepcopy(array)

#Set timer and run function
start = time.time()
sortedArray = serialshellSort(array)
end = time.time()

#printArray(unsortedArray, sortedArray)
print("Time elapsed:", end-start)