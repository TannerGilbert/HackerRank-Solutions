import sys

num_stamps = int(sys.stdin.readline().strip())

s = set()

for _ in range(num_stamps):
    s.add(sys.stdin.readline().strip())

print(len(s))