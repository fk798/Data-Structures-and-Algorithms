from merge import merge

def mergeSort(array):
    if len(array) == 1:
        return array
    half = int(len(array) / 2)
    array1 = mergeSort(array[:half])
    array2 = mergeSort(array[half:])
    return merge(array1, array2)