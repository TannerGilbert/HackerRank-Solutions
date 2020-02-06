import math
import os
import random
import re
import sys


def birthday(s, d, m):
    answer = 0
    for i in range(len(s)):
        j = 0
        count = 0
        while j < m:
            count += s[i+j]
            j += 1
        if count == d:
            answer += 1
        if (i + j) == len(s):
            break
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
