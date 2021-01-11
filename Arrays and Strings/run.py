# given array of numbers, replace each even number with two of the same numbers 

# O(nlogn) solution = append to the end each even number, then sort - this might not be correct if they want the numbers to be in the same positions

# O(n) solution = start from end and double as you go

def reverseTraversal(array):
    # check test cases
    if array == None:
        return None
    
    # increase number of spaces in array
    lengthArray = len(array)
    for i in range(lengthArray):
        if array[i] % 2 == 0:
            array.append(None)

    # get pointers 
    end = len(array)
    i = lengthArray - 1

    # reverse doubling
    while i >= 0:
        if array[i] % 2 == 0:
            end -= 1
            array[end] = array[i]
            end -= 1
            array[end] = array[i]
        else:
            end -= 1
            array[end] = array[i]
        i -= 1
    
    return array

test = [2, 4, 1, 0, 3]
#print(reverseTraversal(test))

#print(reverseTraversal([]))

# this works if the language allows pass by reference - python is pass by object reference so it works
def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

# reverse an array - O(n) time, O(1) space
def reverse(array):
    start = 0
    end = len(array) - 1
    while start < end:
        swap(array, start, end)
        #temp = array[start]
        #array[start] = array[end]
        #array[end] = temp

        start += 1
        end -= 1
    return array

#arr = [2, 4, 1, 3, 8, 6, 5]
#print(reverse(arr))
#print(reverse([]))
#print(reverse(arr))

# Two Sum functions return indices, not the actual values

# assumes array is sorted
def twoSum(array, target): # O(n) time, O(1) space
    start = 0
    end = len(array) - 1
    while start < end:
        sumNum = array[start] + array[end]
        if sumNum < target:
            start += 1
        elif sumNum > target:
            end -= 1
        else:
            return (start, end)
    return None


#print(arr)
#print(twoSum(arr, 10))

# twoSum but O(n) time and O(n) space (due to no assumption of array being sorted)
def twoSumUnsorted(array, target):
    hashTable = {}
    for i in range(len(array)):
        difference = target - array[i]
        if difference in hashTable:
            return (hashTable[difference], i)
        else:
            hashTable[array[i]] = i
    return None

#print(arr)
#print(twoSumUnsorted(arr, 10))

# given a sorted array in non-decreasing order, return array of squares of each number in non-decreasing order - do it in O(n) time

arr = [-4, -2, -1, 0, 3, 5]
# should return [0, 1, 4, 9, 16, 25]

def squaresInc(array): # O(n) space (not possible to do in O(1) space unless you want to sort - O(nlogn) time)
    notInPlace = []
    start = 0
    end = len(array) - 1
    while start < end:
        if abs(array[start]) < abs(array[end]):
            notInPlace.append(array[end] ** 2)
            notInPlace.append(array[start] ** 2)
        else:
            notInPlace.append(array[start] ** 2)
            notInPlace.append(array[end] ** 2)
        start += 1
        end -= 1
    
    return reverse(notInPlace)

print(squaresInc(arr))