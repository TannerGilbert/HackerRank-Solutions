from itertools import product

K, M = list(map(int, input().split()))
arrays = []
for i in range(K):
    arrays.append(list(map(int, input().split())))
    arrays[i].pop(0)

combs = list(product(*arrays))

max_value = 0
for c in combs:
    v = sum([i**2 for i in c]) % M
    if v > max_value:
        max_value = v

print(max_value)
