import math

X, Y = [], []

for _ in range(5):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)
std_X = math.sqrt(sum([(x_i - mean_X)**2 for x_i in X]) / len(X))
std_Y = math.sqrt(sum([(y_i - mean_Y)**2 for y_i in Y]) / len(Y))

pearson_correlation_coefficient = sum([(x_i - mean_X) * (y_i - mean_Y) for x_i, y_i in zip(X, Y)]) / (len(X) * std_X * std_Y)

b = pearson_correlation_coefficient * std_Y / std_X

a = mean_Y - b * mean_X

print(round(a + b * 80, 3))
