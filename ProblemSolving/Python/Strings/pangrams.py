import os


def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    for c in alphabet:
        if c not in s:
            return 'not pangram'
    return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
