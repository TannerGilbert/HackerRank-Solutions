import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    count = 0
    for c in set(ar):
        count += ar.count(c) // 2
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
