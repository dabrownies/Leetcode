"""
max value and a list of integers
return the missing intervals
"""

test = [0,1,2,50,52,75]
test2 = [50]
test3 = [3,70]
test4 = [0,1,2,3,4,5,6,7,8,9]

def getInterval(num1, num2):
    if num1 + 1 == num2 - 1:
        return f"{num1 + 1}"
    else:
        return f"{num1 + 1}-{num2 - 1}"

def missing(arr, max_val):
    if not arr:
        return f"0-{max_val}"
    
    res = []
    if len(arr) == 1:
        if arr[0] == 0:
            return f"1-{max_val}"
        else:
            res.append(getInterval(-1,arr[0]))
            res.append(getInterval(arr[0], max_val+1))
            return res
    # make sure theres at least 2 elements in the array
    if arr[0] != 0:
        res.append(getInterval(-1, arr[0]))
    else:
        for i in range(1, len(arr)):
            if arr[i-1] + 1 == arr[i]:
                continue
            else:
                res.append(getInterval(arr[i-1], arr[i]))

    # if the last element was not the max we need to get that range
    if arr[-1] != max_val:
        res.append(getInterval(arr[-1], max_val + 1))

    return res

print(missing(test, 1000))
print(missing(test2, 75))
print(missing(test3, 70))
print(missing(test4, 10))
