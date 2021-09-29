from collections import Counter

X = int(input())
l = list(map(int, input().split()))
N = int(input())

counts = Counter(l)
total_money = 0

for _ in range(N):
    size, price = list(map(int, input().split()))
    if counts[size] > 0:
        total_money += price
        counts[size] -= 1

print(total_money)
