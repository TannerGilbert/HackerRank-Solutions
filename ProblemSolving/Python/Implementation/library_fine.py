import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
