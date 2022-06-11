from copy import deepcopy
import multiprocessing
import random
import time
from multiprocessing import Pool #https://docs.python.org/3/library/multiprocessing.html

def insertionSort(array):
    '''
    Perform insertion sort of the array. Returns sorted array.
    '''
    edge = 1        #variable to keep track of how many iterations have happened. For optimization purposes
    for i in range(1, len(array)):
        for j in range(0, len(array)-edge):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j] #swap
        edge+=1
    return array

def serialbucketSort(array):
    '''
    Performs a bucket sort of an array (serial implementatiion)
    ''' 
    n = len(array)  
    cpuCount = multiprocessing.cpu_count()
    bucket = [[] for _ in range(cpuCount)]       #amount of buckets is based on the whole numbers within the range
    sort = []                               #output array
    for i in array:
        #arranges elements to *cpuCount* buckets based on its rounded-down whole number value
        if i > 0:
            multiplier = 0
            while(cpuCount//2 > multiplier):
                if(i >= ((multiplier*n)//cpuCount)) and (i < ((multiplier+1)*n)//cpuCount):
                    bucket[multiplier+int(cpuCount//2)].append(i)
                    break
                multiplier+=1
        else:
            multiplier = (cpuCount//2)*-1
            while(multiplier < 0):
                if(i >= ((multiplier*n)//cpuCount)) and (i < ((multiplier+1)*n)//cpuCount):
                    bucket[int(cpuCount//2)+multiplier].append(i)
                    break
                multiplier+=1
            

    pool = Pool(processes=cpuCount)
    sorted = pool.map(insertionSort,[i for i in bucket])    #parallel core-affine threads with insertionSort as a subroutine
    for i in sorted:                                        #will process each bucket parallelly
        for j in i:
            sort.append(j)
    return sort
 
N = int(input("Enter array size: "))
array = []
for i in range(N):
    array.append(round(random.uniform(-N//2, N//2), 2))   #Generate randomized array
unsortedArray = deepcopy(array)

#Set timer and run function
start = time.time()
sortedArray = serialbucketSort(array)
end = time.time()

#print("Unsorted Array:",unsortedArray)      #Print unsorted array (output)
#sprint("Sorted Array:  ",sortedArray)      #Print sorted array(output)
print("Time elapsed:", end-start)