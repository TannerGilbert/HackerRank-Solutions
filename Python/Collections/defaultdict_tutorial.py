from collections import defaultdict

n, m = list(map(int, input().split()))
A = defaultdict(list)
for i in range(n):
    A[input()].append(i+1)
B = [input() for i in range(m)]

for i in B:
    if i in A:
        print(*A[i])
    else:
        print(-1)
