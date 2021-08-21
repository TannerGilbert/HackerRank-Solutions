def partition(arr):
    p = arr[0]
    left, equal, right = [], [], []
    
    for e in arr:
        if e > p:
            right.append(e)
        elif e == p:
            equal.append(e)
        else:
            left.append(e)
    return left, equal, right


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    left, equal, right = partition(arr)
    
    arr = quicksort(left) + equal + quicksort(right)
    print(*arr)
    
    return arr

n = int(input())
ar = list(map(int, input().split()))

quicksort(ar)
