n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

X_sorted = sorted(X)
Y_sorted = sorted(Y)

r_x = [X_sorted.index(x) + 1 for x in X]
r_y = [Y_sorted.index(y) + 1 for y in Y]

print(round(1 - 6 * sum([(x - y)**2 for x, y in zip(r_x, r_y)]) / (n * (n**2 - 1)), 3))
