from itertools import combinations_with_replacement

string, size = input().split()
size = int(size)

comb = list(map(lambda x: ''.join(x), list(combinations_with_replacement(sorted(list(string)), size))))

for c in comb:
    print(c)