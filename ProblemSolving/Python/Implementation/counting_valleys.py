import math
import os
import random
import re
import sys


def countingValleys(n, s):
    count = 0
    height = 0
    old_height = 0

    for i in s:
        height += 1 if i == 'U' else -1
        if height == -1 and old_height == 0:
            count += 1
        old_height = height
    return count 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
