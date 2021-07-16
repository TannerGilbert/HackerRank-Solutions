#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0

    for apple in apples:
        if a + apple >= s and a + apple <= t:
            apples_count += 1

    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            oranges_count += 1

    print(apples_count)
    print(oranges_count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
