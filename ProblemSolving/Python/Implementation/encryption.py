import math
import os


def encryption(s):
    num_rows = math.floor(math.sqrt(len(s)))
    num_columns = math.ceil(math.sqrt(len(s)))
    
    encoded = ''
    
    for c1 in range(num_columns):
        for c2 in range(num_columns):
            if c1 + c2 * num_columns >= len(s):
                break
            encoded += s[c1 + c2 * num_columns]
        encoded += ' '
    
    return encoded


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
