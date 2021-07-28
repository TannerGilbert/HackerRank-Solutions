import os
from collections import Counter


def equalizeArray(arr):
    cnt = Counter(arr)
    count = 0
    for i, v in cnt.most_common()[1:]:
        count += v
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
