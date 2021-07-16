import math
import os
import random
import re
import sys


def appendAndDelete(s, t, k):
    start_index = 0
    to_delete = 0
    to_append = 0

    while start_index < len(s) and start_index < len(t) and s[start_index] == t[start_index]:
        start_index += 1

    if start_index < len(s):
        to_delete = len(s[start_index:])
        if to_delete == len(s) and k - to_delete >= len(t):
            return 'Yes'

    if start_index < len(t):
        to_append = len(t[start_index:])

    k -= to_delete + to_append

    if k == 0 or (k > 0 and k % 2 == 0) or k >= 2*len(t):
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
