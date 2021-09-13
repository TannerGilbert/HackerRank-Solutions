import os


def strangeCounter(t):
    max_count = 3
    while t > max_count:
        t -= max_count
        max_count = max_count * 2
    
    return max_count - t + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
