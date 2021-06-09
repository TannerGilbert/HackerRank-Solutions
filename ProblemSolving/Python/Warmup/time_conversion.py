import os
import sys


def timeConversion(s):
    code = s[-2:]

    if code == 'PM' and not s.startswith('12'):
        s = str(int(s[:2]) + 12) + s[2:]
    if s.startswith('12') and s.endswith('AM'):
        s = '00' + s[2:]
    return s[:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
