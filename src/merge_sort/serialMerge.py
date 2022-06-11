from copy import deepcopy
import random
import time

def serialmergeSort(array):
    '''
    Sort the list of integers through the Merge Sort Algorithm (Serial Implementation)
    '''
    i = 0           #to keep track of the index to be changed
    if len(array) > 1:
        # Finding the mid of the array
        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]
 
        # recursively sorting the both halves 
        serialmergeSort(L)
        serialmergeSort(R)

 
        # merge sorted arrays (while sorting)
        while (len(L) > 0) and (len(R) > 0):
            if(L[0] >= R[0]):
                array[i] = R[0]
                R.pop(0)
            elif(R[0] >= L[0]):
                array[i] = L[0]
                L.pop(0)
            i+=1

        #incorporate whatever that's left
        while(len(L) > 0):
            array[i] = (L[0])
            L.pop(0)
            i+=1
        
        while(len(R) > 0):
            array[i] = (R[0])
            R.pop(0)
            i+=1
 
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
serialmergeSort(array)
end = time.time()

#printArray(unsortedArray, sortedArray)
print("Time elapsed:", end-start)