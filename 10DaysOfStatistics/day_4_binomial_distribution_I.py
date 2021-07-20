import math

inp = list(map(float, input().split()))
p = inp[0] / sum(inp)
result = 0

for i in range(3, 7):
    result += math.factorial(6) / (math.factorial(i) * math.factorial(6-i)) * math.pow(p, i) * math.pow(1-p, 6-i)

print(round(result, 3))
