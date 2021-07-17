import math
import os
import random
import re
import sys


def calculate_median(arr):
    middle = int(len(arr)/2)
    if len(arr) % 2 == 0:
        return int((arr[middle-1] + arr[middle]) / 2)
    else:
        return arr[middle]


def interQuartile(values, freqs):
    # https://stackoverflow.com/a/29244613/9610844
    dataset = sum([[v] * f for v, f in zip(values, freqs)], [])

    dataset.sort()
    middle = int(len(dataset)/2)

    q1 = calculate_median(dataset[:middle])
    median = calculate_median(dataset)
    if len(dataset) % 2 == 0:
        q3 = calculate_median(dataset[middle:])
    else:
        q3 = calculate_median(dataset[middle+1:])

    print("{:.1f}".format(round(q3 - q1, 1)))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
