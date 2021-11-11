import os


def marsExploration(s):
    count = 0
    for i in range(int(len(s) / 3)):
        count += int(s[i*3] != 'S') + int(s[i*3+1]
                                          != 'O') + int(s[i*3+2] != 'S')
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
