import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    print(fac)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
