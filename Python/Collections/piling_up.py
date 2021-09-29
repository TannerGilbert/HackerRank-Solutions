from collections import deque
import math

T = int(input())

for _ in range(T):
    n = int(input())
    last = math.inf
    d = deque(list(map(int, input().split())))
    possible = True
    while len(d) > 0:
        ind = 0 if d[0] > d[-1] and d[0] <= last else -1
        if d[ind] <= last:
            last = d.popleft() if d[0] > d[-1] else d.pop()
        else:
            possible = False
            break
    print('Yes' if possible else 'No')
