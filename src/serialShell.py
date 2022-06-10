from copy import deepcopy
import random
import time

def serialshellSort(array):
    index = 0
    gap = len(array)//2

    while gap > 0:
        if (index + gap) < len(array):
            if(array[index] > array[index+gap]):
                array[index], array[index+gap] = array[index+gap], array[index]
            index+=1
        else:
            index = 0
            gap = gap//2
    return array
 
 
 
 
 
N = int(input("Enter array size: "))
array = []
for i in range(N):
    array.append(random.randint(-N//2, N//2))   #Generate rnaodmized array
unsortedArray = deepcopy(array)

#Set timer and run function
start = time.time()
sortedArray = serialshellSort(array)
end = time.time()

#print("Unsorted Array:",unsortedArray)      #Print unsorted array
#print("Sorted Array:  ",sortedArray)      #Print sorted array
print("Time elapsed:", end-start)