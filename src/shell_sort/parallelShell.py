from copy import deepcopy
import random
import time
import multiprocessing
from multiprocessing import Pool #https://docs.python.org/3/library/multiprocessing.html
import numpy

def shellSort(array):
    '''
    Perfom shell sort of an array with length n. Initial gap is n/2. Subroutine for parallel execution
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

def parallelshellSort(array):
    '''
    Parallel Shell sort. array will be divided into equal-ish parts based on number of CPUs
    Shell sort will be implemented on each partition parallelly then merged. Repeat until sorted.
    '''
    cpuCount = multiprocessing.cpu_count()
    merged = []

    while cpuCount > 0:
        merged = []
        partitions = numpy.array_split(array, cpuCount) #partition array to cpuCount equal-ish parts
        pool = Pool(processes=cpuCount) #for shellSort
        sorted = pool.map(shellSort,[i for i in partitions])    #parallel core-affine threads with shellSort as a subroutine
        pool.close()
        pool.join()
        for i in sorted:
            for j in i:
                merged.append(j)
        cpuCount = cpuCount//2

    return merged

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
sortedArray = parallelshellSort(array)
end = time.time()

#printArray(unsortedArray, sortedArray)
print("Time elapsed:", end-start)