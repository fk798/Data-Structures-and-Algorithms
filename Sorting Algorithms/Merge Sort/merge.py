# implementation of merge function for merge sort

# assumes a and b are already sorted
def merge(a, b):
    res = []
    pointerA, pointerB = 0, 0
    while pointerA != len(a) and pointerB != len(b):
        if a[pointerA] <= b[pointerB]:
            res.append(a[pointerA])
            pointerA += 1
        else:
            res.append(b[pointerB])
            pointerB += 1
    # get the elements that are left to append
    if pointerA != len(a):
        while pointerA != len(a):
            res.append(a[pointerA])
            pointerA += 1
    elif pointerB != len(b):
        while pointerB != len(b):
            res.append(b[pointerB])
            pointerB += 1
    return res