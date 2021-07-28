import math
import os
import random
import re
import sys


def permutationEquation(p):
    result = []
    for i in range(1, len(p)+1):
        ind = p.index(i)
        result.append(p.index(ind + 1) +1 )
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
