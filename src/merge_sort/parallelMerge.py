from copy import deepcopy
import multiprocessing
import random
import time
from multiprocessing import Pool #https://docs.python.org/3/library/multiprocessing.html

def mergeArray(L, R):
    '''
    Merge two sorted Arrays
    '''
    # merge sorted arrays (while sorting)
    array = []
    while (len(L) > 0) and (len(R) > 0):
        if(L[0] >= R[0]):
            array.append(R[0])
            R.pop(0)
        elif(R[0] >= L[0]):
            array.append(L[0])
            L.pop(0)

    #incorporate whatever that's left
    while(len(L) > 0):
        array.append(L[0])
        L.pop(0)
        
    while(len(R) > 0):
        array.append(R[0])
        R.pop(0)
    
    return array

def mergeSort(array):
    '''
    Sort the list of integers through the Merge Sort Algorithm (Subroutine)
    '''
    i = 0           #to keep track of the index to be changed
    if len(array) > 1:
        # Finding the mid of the array
        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]
 
        # recursively sorting the both halves 
        mergeSort(L)
        mergeSort(R)

        array = mergeArray(L, R)
    return array
 
def parallelmergeSort(array):
    '''
    Sort the list of integers through the Merge Sort Algorithm (Parallel Implementation)
    '''
    n = len(array)
    cpuCount = multiprocessing.cpu_count()
    subArray = [[] for _ in range(cpuCount)]       #amount of buckets is based on the whole numbers within the range

    partition = 0
    index = 0
    extra = n%cpuCount
    while (index < cpuCount):       #partition data to p parts where p is the number of cores
        if index >= extra:
            subArray[index] = array[partition:partition+(n//cpuCount)]
            partition+=(n//cpuCount)
        else:
            subArray[index] = array[partition:partition+(n//cpuCount)+1]
            partition+=(n//cpuCount)+1
        index+=1

    pool = Pool(processes=cpuCount)
    sorted = pool.map(mergeSort,[i for i in subArray])    #parallel core-affine threads with insertionSort as a subroutine
    pool.close()
    pool.join()
    
    #merge all remaining sorted arrrays
    while(len(sorted) > 1):
        sorted[0] = mergeArray(sorted[0], sorted[1])
        sorted.pop(1)
    
    return sorted[0]

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
sortedArray = parallelmergeSort(array)
end = time.time()

#printArray(unsortedArray, sortedArray)
print("Time elapsed:", end-start)