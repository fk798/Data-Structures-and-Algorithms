#from merge import merge
from mergesort import mergeSort
import random 

#array1 = [1, 3, 5, 7, 9]
#array2 = [2, 4, 6, 8, 10]

#print(merge(array1, array2))

#array1 = [1, 3, 5, 7, 9]
#array2 = [1, 3, 4, 5, 7, 9]

#print(merge(array1, array2))

#assert(merge(array1, array2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

array = []
for i in range(100):
    array.append(random.randint(0, 100))

print(mergeSort(array) == sorted(array))