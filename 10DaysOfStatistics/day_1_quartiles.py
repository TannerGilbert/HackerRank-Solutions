import math
import os
import random
import re
import sys


def calculate_median(arr):
    middle = int(len(arr)/2)
    if len(arr) % 2 == 0:
        return int((arr[middle-1] + arr[middle]) / 2)
    else:
        return arr[middle]


def quartiles(arr):
    arr.sort()
    middle = int(len(arr)/2)

    q1 = calculate_median(arr[:middle])
    median = calculate_median(arr)
    if len(arr) % 2 == 0:
        q3 = calculate_median(arr[middle:])
    else:
        q3 = calculate_median(arr[middle+1:])

    return q1, median, q3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
