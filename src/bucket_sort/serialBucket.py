from copy import deepcopy
import random
import time

def ssort(array):
    '''
    Returns sorted array.
    '''
    return sorted(array)

def serialbucketSort(array):
    '''
    Performs a bucket sort of an array (serial implementatiion)
    ''' 
    n = len(array)  
    bucket = [[] for x in range(n+1)]       #amount of buckets is based on the whole numbers within the range
    sort = []                               #output array
    for i in array:
        bucket[int(i//1)+n//2].append(i)    #arranges elements to buckets based on its rounded-down whole number value
    
    for i in bucket:                        #perform insertiion sort on each buckets then append it on output
        sortBucket = ssort(i)
        for i in sortBucket:
            sort.append(i)

    return sort
 
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
sortedArray = serialbucketSort(array)
end = time.time()

#printArray(unsortedArray, sortedArray)
print("Time elapsed:", end-start)