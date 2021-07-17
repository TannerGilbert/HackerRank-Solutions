n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().strip()
    if command == 'pop':
        s.pop()
    elif command.startswith('discard'):
        s.discard(int(command.split(' ')[1]))
    elif command.startswith('remove'):
        s.remove(int(command.split(' ')[1]))


print(sum(s))
