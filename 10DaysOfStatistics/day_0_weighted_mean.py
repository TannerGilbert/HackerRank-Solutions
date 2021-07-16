import math
import os
import random
import re
import sys


def weightedMean(X, W):
    weighted_mean = sum([x_i * w_i for x_i, w_i in zip(X, W)]) / sum(W)
    print(round(weighted_mean, 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
