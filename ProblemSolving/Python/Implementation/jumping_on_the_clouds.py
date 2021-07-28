import os


def jumpingOnClouds(c):
    current_position = 0
    count = 0
    while current_position < len(c) - 1:
        if len(c) - 1 <= current_position +2:
            current_position = len(c) - 1
            count += 1
            break
        elif c[current_position+2] == 0:
            current_position += 2
            count += 1
        else:
            current_position += 1
            count += 1   
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
