import os


def gameOfThrones(s):
    unique_chars = list(set(s))
    count = 0
    for c in unique_chars:
        if s.count(c) % 2 == 1:
            count += 1
        if count > 1:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
