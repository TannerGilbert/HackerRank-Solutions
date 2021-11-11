import os
import functools


def shift_char(c, alphabet, new_order):
    if c.isalpha():
        if c.isupper():
            return new_order[alphabet.index(c.lower())].upper()
        return new_order[alphabet.index(c)]
    return c


def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = k % len(alphabet)
    new_order = alphabet[k:] + alphabet[:k]
    return ''.join(list(map(functools.partial(shift_char, alphabet=alphabet, new_order=new_order),  list(s))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
