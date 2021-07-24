import math


def pearson_correlation_coefficient(X, Y):
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)
    std_X = math.sqrt(sum([(x_i - mean_X)**2 for x_i in X]) / len(X))
    std_Y = math.sqrt(sum([(y_i - mean_Y)**2 for y_i in Y]) / len(Y))

    return sum([(x_i - mean_X) * (y_i - mean_Y) for x_i, y_i in zip(X, Y)]) / (len(X) * std_X * std_Y)


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print(round(pearson_correlation_coefficient(X, Y), 3))
