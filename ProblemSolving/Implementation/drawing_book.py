import os
import sys
import math


def pageCount(n, p):
    front_count = math.ceil((p - 1) / 2)
    if n % 2 == 1:
        n -= 1
    back_count = math.ceil((n - p) / 2)

    return min([front_count, back_count]) 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
