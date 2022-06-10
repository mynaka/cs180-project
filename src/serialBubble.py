import random
import time

def serialbubbleSort(array):
    '''
    #Sort the list of integers through the Bubble Sort Algorithm (Serial Implementation)
    '''
    size = len(array)

    for i in range(size):
        swap = False            #reset swap flag to false
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] #Swap list elements
                swap = True                                 #Set swap flag to true
        if not swap:       #If swap remains false, break loop
            break          #This means that the array is already sorted
    return array

N = int(input("Enter array size: "))
unsortedArray = []
for i in range(N):
    unsortedArray.append(random.randint(-N//2, N//2))   #Generate rnaodmized array

#Set timer and run function
start = time.time()
sortedArray = serialbubbleSort(unsortedArray)
end = time.time()

#print(sortedArray)      #Print sorted array
print("Time elapsed:", end-start)