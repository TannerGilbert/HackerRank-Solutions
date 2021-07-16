import math
import os
import random
import re
import sys


def cutTheSticks(arr):
    num = []
    while len(arr) != 0:
        num.append(len(arr))
        min_value = min(arr)
        arr = list(map(lambda x: x-min_value, arr))
        arr = list(filter(lambda x: x > 0, arr))
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
