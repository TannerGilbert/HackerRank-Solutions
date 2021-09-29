from collections import deque

N = int(input())
d = deque()

for _ in range(N):
    inp = input().split()
    
    if len(inp) == 2:
        operation = inp[0]
        num = int(inp[1])
    else:
        operation = inp[0]
        num = 0
    
    if operation == 'append':
        d.append(num)
    elif operation == 'appendleft':
        d.appendleft(num)
    elif operation == 'pop':
        d.pop()
    elif operation == 'popleft':
        d.popleft()

print(*d)