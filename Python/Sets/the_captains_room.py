import time

start = time.time()

K = int(input())
l = list(map(int, input().split()))

print((sum(set(l)) * K - sum(l)) // (K - 1))
