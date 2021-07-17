A = set(map(int, input().split()))
n = int(input())
strict_subset = True

for _ in range(n):
    B = set(map(int, input().split()))
    if len(A.difference(B)) < 1 or len(B.difference(A)) != 0:
        strict_subset = False
        break

print(strict_subset)