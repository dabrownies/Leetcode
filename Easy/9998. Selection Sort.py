"""9998. Selection Sort"""

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_num = arr[i]
        min_ndx = i

        for j in range(i+1, len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                min_ndx = j

        temp = arr[i]
        arr[i] = min_num
        arr[min_ndx] = temp

test = [5,63,6,4,3,6,90]
print(test)
selectionSort(test)
print(test)




