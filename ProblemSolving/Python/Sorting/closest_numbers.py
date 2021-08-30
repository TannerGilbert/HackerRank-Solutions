import math
import os


def closestNumbers(arr):
    arr.sort()
    min_distance = math.inf
    min_pairs = []
    for i in range(len(arr)-1):
        v, v2 = arr[i], arr[i+1]
        if abs(v-v2) < min_distance:
            min_distance = abs(v-v2)
            min_pairs = [v, v2]
        elif abs(v-v2) == min_distance and not (v in min_pairs and v2 in min_pairs):
            min_pairs.extend((v, v2))
    return min_pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
