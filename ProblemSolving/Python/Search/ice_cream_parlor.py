import os


def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if i != j and arr[i] + arr[j] == m:
                return [i+1, j+1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
