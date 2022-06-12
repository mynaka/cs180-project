from copy import deepcopy
import random
import time
from multiprocessing import Pool

def checkSorted(array):
    sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            sorted = False
            break
    return sorted

def swap(array):
    '''
    Sorts a 2-element array or 1-element array. Subroutine for parallel bubble sort
    '''
    if (len(array) == 1):
        return array
    elif (array[0] > array[1]):
        array[0], array[1] = array[1], array[0]
    return array

def parallelBubble(array):
    '''
    Sorts the array using bubble sort parallelly. There are two phases in the sorting.
    The array will be partitioned to pairs depending on the phase then each partition
    will be parallelly sorted and remerged. Repeat until sorted
    '''
    rem = len(array)%2          #determines whether array length is odd or even
    partition = []              #partition for data
    sorted = []
    newArray = array           #gets new state of array per iteration
    evenFlag = True
    while not(checkSorted(newArray)):
        partition = []
        if evenFlag:
            p = len(array)//2
            pool = Pool(processes=p+1)

            if rem == 1:
                end = -2
            else:
                end = -1

            index = 0
            while(index < len(newArray)+end):  #partition array into pairs depending on the phase of the sorting
                partition.append([newArray[index], newArray[index+1]])
                index+=2

            if end == -2:
                partition.append([newArray[-1]])

            sorted = pool.map(swap,[i for i in partition])    #parallel core-affine threads with insertionSort as a subroutine
            pool.close()
            pool.join()
            evenFlag = False
        else:
            if rem == 1:
                p = len(newArray)//2
                end = -1
            else:
                p = (len(newArray)//2)-1
                end = -2

            partition.append([newArray[0]])
            index = 1
            while(index < len(newArray)+end):  #partitions
                partition.append([newArray[index], newArray[index+1]])
                index+=2

            if(end == -2):
                partition.append([array [-1]])

            pool = Pool(processes=p+1)
            sorted = pool.map(swap,[i for i in partition])    #parallel core-affine threads with insertionSort as a subroutine
            pool.close()
            pool.join()
            evenFlag = True
        
        newArray = []
        for i in sorted:
            for j in i:
                newArray.append(j)
    return (newArray)
        

def printArray(unsortedArray, sortedArray):
    '''
    Print input and output arrays
    '''
    print("Unsorted Arrray:",unsortedArray)    #Print unsorted array
    print("Sorted Array:   ",sortedArray)      #Print sorted array(output)

N = int(input("Enter array size: "))
unsortedArray = []
for i in range(N):
    unsortedArray.append(round(random.uniform(-N//2, N//2), 2))   #Generate randomized array

#Set timer and run function
start = time.time()
sortedArray = parallelBubble(unsortedArray)
end = time.time()

#printArray(unsortedArray, sortedArray)
print("Time elapsed:", end-start)