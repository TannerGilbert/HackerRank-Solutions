import math


def cumulative_normal_distribution(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


mu, sigma = list(map(float, input().split()))
n1 = float(input())
n2, n3 = list(map(float, input().split()))

print(round(cumulative_normal_distribution(n1, mu, sigma), 3))
print(round(cumulative_normal_distribution(n3, mu, sigma) - cumulative_normal_distribution(n2, mu, sigma), 3))
