from itertools import combinations

string, size = input().split()
size = int(size)

for i in range(1, size+1):
    comb = list(map(lambda x: ''.join(x), list(combinations(sorted(list(string)), i))))
    for c in comb:
        print(c)
