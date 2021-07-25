import numpy as np


m, n = list(map(int, input().split()))

X = []
Y = []

for _ in range(n):
    l = list(map(float, input().split()))
    X.append([1] + l[:-1])
    Y.append(l[-1])
    
X = np.asarray(X)
Y = np.asarray(Y)

B = np.dot(np.dot(np.linalg.inv(np.dot(X.transpose(), X)), X.transpose()), Y)

q = int(input())

for _ in range(q):
    X = np.asarray([1] + list(map(float, input().split())))
    print(np.dot(X, B))