import math


def binomial_distribution(x, n, p):
    return sum([math.factorial(n) / (math.factorial(r) * math.factorial(n - r)) * math.pow(p, r) * math.pow(1 - p, n - r) for r in range(x, n + 1)])


inp = list(map(int, input().split()))
pct = inp[0] / 100.

print(round(1 - binomial_distribution(3, inp[1], pct), 3))
print(round(binomial_distribution(2, inp[1], pct), 3))
