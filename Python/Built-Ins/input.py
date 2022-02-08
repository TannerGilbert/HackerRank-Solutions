x, k = list(map(int, input().split()))
P = input()

print(eval(P.replace('x', str(x))) == k)
