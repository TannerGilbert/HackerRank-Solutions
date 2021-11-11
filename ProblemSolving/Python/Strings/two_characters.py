import os
import itertools


def is_alternating(s):
    for i in range(len(s) - 2):
        if s[i] != s[i+2]:
            return False

    if s[0] == s[1]:
        return False

    return True


def alternate(s):
    unique_chars = list(set(s))
    if len(unique_chars) == 1:
        return 0
    comb = itertools.combinations(unique_chars, len(unique_chars) - 2)
    max_length = 0
    for c in comb:
        filtered_str = ''.join(filter(lambda x: x not in c, s))
        if is_alternating(filtered_str) and len(filtered_str) > max_length:
            max_length = len(filtered_str)
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
