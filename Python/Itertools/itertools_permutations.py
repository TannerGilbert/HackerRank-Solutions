from itertools import permutations

string, size = input().split()
size = int(size)

per = sorted(list(map(lambda x: ''.join(x), list(permutations(string, size)))))

for p in per:
    print(p)
