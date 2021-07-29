
import os
import re


def camelcase(s):
    return len(re.findall('[A-Z][a-z]*', s)) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
