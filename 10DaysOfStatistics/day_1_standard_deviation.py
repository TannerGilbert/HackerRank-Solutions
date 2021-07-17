import math
import os
import random
import re
import sys


def stdDev(arr):
    mean = sum(arr) / len(arr)
    std = math.sqrt(sum([(v - mean) ** 2 for v in arr]) / len(arr))
    print('{:.1f}'.format(std))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
