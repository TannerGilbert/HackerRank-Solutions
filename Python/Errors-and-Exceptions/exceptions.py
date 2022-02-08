T = int(input())

for _ in range(T):
    a, b = list(input().rstrip().split())
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)
