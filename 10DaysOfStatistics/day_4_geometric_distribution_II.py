import math


def binomial_distribution(x, n, p):
    return sum([math.factorial(n) / (math.factorial(r) * math.factorial(n - r)) * math.pow(p, r) * math.pow(1 - p, n - r) for r in range(x, n + 1)])


inp = list(map(int, input().split()))
p = inp[0] / inp[1]

n = int(input())

print(round(binomial_distribution(1, n, p), 3))
