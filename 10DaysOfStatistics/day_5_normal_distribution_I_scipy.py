import math
import scipy.integrate as integrate


def cumulative_normal_distribution(x, mu, sigma):
    def erf(z):
        return 2 / math.sqrt(math.pi) * integrate.quad(lambda x: math.pow(math.e, -math.pow(x, 2)), 0, z)[0]

    return 0.5 * (1 + erf((x - mu) / (sigma * math.sqrt(2))))


mu, sigma = list(map(float, input().split()))
n1 = float(input())
n2, n3 = list(map(float, input().split()))

print(round(cumulative_normal_distribution(n1, mu, sigma), 3))
print(round(cumulative_normal_distribution(n3, mu, sigma) - cumulative_normal_distribution(n2, mu, sigma), 3))
