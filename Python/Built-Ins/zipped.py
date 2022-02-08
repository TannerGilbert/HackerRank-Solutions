N, X = list(map(int, input().split()))


arr = []
for i in range(X):
    arr.append(list(map(float, input().split())))

for i in zip(*arr):
    print(sum(i) / len(i))
