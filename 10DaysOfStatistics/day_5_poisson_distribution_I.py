import math


def poisson_distribution(k, l):
    return math.pow(l, k) * math.pow(math.e, -l) / math.factorial(k)


l = float(input())
k = float(input())

print(round(poisson_distribution(k, l), 3))
