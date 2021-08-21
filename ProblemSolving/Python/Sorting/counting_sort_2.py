import os


def countingSort(arr):
    freq = [0] * 100
    for i in arr:
        freq[i] += 1
    ar = []
    for i, v in enumerate(freq):
        ar = ar + [i] * v
    return ar


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
