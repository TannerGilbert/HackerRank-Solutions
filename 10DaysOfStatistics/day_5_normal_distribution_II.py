import math


def cumulative_normal_distribution(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


mu, sigma = list(map(float, input().split()))
n1 = float(input())
n2 = float(input())

print(round((1 - cumulative_normal_distribution(n1, mu, sigma)) * 100, 2))
print(round((1 - cumulative_normal_distribution(n2, mu, sigma)) * 100, 2))
print(round(cumulative_normal_distribution(n2, mu, sigma) * 100, 2))
