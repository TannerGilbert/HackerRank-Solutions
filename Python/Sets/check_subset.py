T = int(input())

for _ in range(T):
    a_len = int(input())
    a = set(map(int, input().split()))
    b_len = int(input())
    b = set(map(int, input().split()))
    print(len(a.difference(b)) == 0)
