import math
import os
import random
import re
import sys


def utopianTree(n):
    height = 1
    for i in range(1, n+1):
        height += 1 if i % 2 == 0 else height
    return height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
