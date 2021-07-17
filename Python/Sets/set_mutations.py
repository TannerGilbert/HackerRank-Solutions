A_len = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, set_length = input().split()
    s = set(map(int, input().split()))
    if operation == 'intersection_update':
        A.intersection_update(s)
    elif operation == 'update':
        A.update(s)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(s)
    elif operation == 'difference_update':
        A.difference_update(s)

print(sum(A))
