import math
import os
import random
import re
import sys


def jumpingOnClouds(c, k):
    e = 100
    index = 0
    while True:
        index += k
        if c[index % len(c)] == 1:
            e -= 2
        e -= 1
        if index % len(c) == 0:
            break
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
