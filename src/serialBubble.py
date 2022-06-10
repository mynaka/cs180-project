import random

def serialbubbleSort(array):
    size = len(array)

    for i in range(size):
        swap = False
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if not swap:
            break
    return array

N = int(input("Enter array size: "))
unsorted = []
for i in range(N):
    unsorted.append(random.randint(-N//2, N//2))
print(serialbubbleSort(unsorted))