import math


def kaprekarNumbers(p, q):
    kaprekar_nums = []
    
    for n in range(p, q+1):
        d = len(str(n))
        n_squared = int(math.pow(n, 2))
        n_squared_str = str(n_squared)
        if len(n_squared_str) >= 2:
            l = int(n_squared_str[:d-1]) if len(n_squared_str) % 2 == 1 else int(n_squared_str[:d])
            r = int(n_squared_str[d-1:]) if len(n_squared_str) % 2 == 1 else int(n_squared_str[d:])
        if n == 1 or (n > 3 and l + r == n):
            kaprekar_nums.append(str(n))
    
    if len(kaprekar_nums) >= 1:
        print(' '.join(kaprekar_nums))
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
