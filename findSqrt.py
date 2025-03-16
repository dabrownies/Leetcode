# edge case 1: if given 0, return 0
# edge case 2: negative values
# 25 -> 5




def findSqrt(x):
    if x < 0:
        return -1
    
    if x == 0:
        return 0
    
    # valid number
    j = 1
    while j * j < x:
        j += 1

    return j - 1