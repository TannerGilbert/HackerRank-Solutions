#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    a = sorted(a)
    unique = set(a)
    count = 0
    counts = []
    for u in unique:
        for i in a:
            if i == u or i == u+1:
                count += 1
        counts.append(count)
        count = 0
    return max(counts)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
