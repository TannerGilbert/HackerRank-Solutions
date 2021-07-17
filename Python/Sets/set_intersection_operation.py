n = int(input())
a1 = set(map(int, input().split()))
n2 = int(input())
a2 = set(map(int, input().split()))

print(len(a1.intersection(a2)))
