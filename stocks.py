test = [2, -4, 8]

def drop(arr):
    biggest_drop = float('inf')
    curr = 0

    for price in arr:
        curr += price

        biggest_drop = min(biggest_drop, curr)
        if curr > 0:
            curr = 0
    
    return biggest_drop

print(drop(test))