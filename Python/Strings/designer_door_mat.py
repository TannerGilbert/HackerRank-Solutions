N, M = list(map(int, input().rstrip().split()))

for i in range(1, N, 2):
    print((M-i*3)//2 * '-' + i * '.|.' + (M-i*3)//2 * '-')

print((M-7)//2 * '-' + 'WELCOME' + (M-7)//2 * '-')

for i in reversed(range(1, N, 2)):
    print((M-i*3)//2 * '-' + i * '.|.' + (M-i*3)//2 * '-')
