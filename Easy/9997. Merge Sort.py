"""9997. Merge Sort"""

def mergeSort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    leftArr = [num for num in arr[:mid]]
    rightArr = [num for num in arr[mid:len(arr)]]

    mergeSort(leftArr)
    mergeSort(rightArr)
    merge(arr, leftArr, rightArr)

    return arr

# merging
def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # still more values in left
    if i < len(left):
        while i != len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    # still more values in right
    if j < len(right):
        while j != len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


test = [5,3,55,3,6,3,54,34,7,34,1,2]
print(test)
mergeSort(test)
print(test)