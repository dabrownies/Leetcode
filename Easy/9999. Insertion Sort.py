"""9999. Insertion Sort"""

def insertionSort(arr):
    for i in range(1, len(s)):
        curr = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1

    arr[j+1] = curr

test = [6,43,3,6,43,65,3]
print(test)
insertionSort(test)
print(test)

