import sys

a_size = sys.stdin.readline()
a = set(list(map(int, sys.stdin.readline().split(' '))))
b_size = sys.stdin.readline()
b = set(list(map(int, sys.stdin.readline().split(' '))))

symmetric_difference = a.difference(b).union(b.difference(a))

for i in sorted(symmetric_difference):
    print(i)