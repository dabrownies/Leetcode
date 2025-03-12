import random

def quicksort(A, low, high):
    # theres only 1 element which is already sorted
    if low >= high:
        return 
    
    
    # get a random pivot
    pivot_index = random.randint(low, high)
    pivot = A[pivot_index]
    swap(A, pivot_index, high)

    l = low
    r = high

    while l < r:
        while A[l] <= pivot and l < r:
            l += 1
        
        while A[r] >= pivot and l < r:
            r -= 1

        swap(A, l, r) # swap left with right

    swap(A, l, high) # swap left with pivot

    # recursively quicksort left side of the pivot, and right side of pivot
    quicksort(A, low, l - 1)
    quicksort(A, l + 1, high)

    return A

def swap(A, ndx1, ndx2):
    A[ndx1], A[ndx2] = A[ndx2], A[ndx1]





test = [6,3,45,3,67,36,37,327,745,234]
print(test)
quicksort(test, 0, len(test) - 1)
print(test)