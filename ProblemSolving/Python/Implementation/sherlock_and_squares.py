import math
import os
import random
import re
import sys


def squares(a, b):
    a_sqrt = math.sqrt(a)
    b_sqrt = math.sqrt(b)
    if a_sqrt.is_integer() and not b_sqrt.is_integer():
        return abs(math.floor(a_sqrt) - math.ceil(b_sqrt))
    if a_sqrt.is_integer() and b_sqrt.is_integer():
        return abs(math.floor(a_sqrt) - math.ceil(b_sqrt)) + 1
    return abs(math.floor(a_sqrt) - math.floor(b_sqrt))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
