import math

inp = list(map(int, input().split()))
p = inp[0] / inp[1]

n = int(input())

print(round(math.pow(1-p, n-1)*p, 3))
