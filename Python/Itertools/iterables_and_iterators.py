from itertools import combinations

N = int(input())
arr = list(input().strip().split())
K = int(input())

comb = list(combinations(sorted(arr), K))
filtered = list(filter(lambda x: 'a' in x, comb))

print(len(filtered)/len(comb))
