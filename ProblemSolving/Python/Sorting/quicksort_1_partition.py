import os


def quickSort(arr):
    p = arr[0]
    left, equal, right = [], [], []
    
    for e in arr:
        if e > p:
            right.append(e)
        elif e == p:
            equal.append(e)
        else:
            left.append(e)
    
    return left + equal + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
