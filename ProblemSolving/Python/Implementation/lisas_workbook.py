import os


def workbook(n, k, arr):
    count = 0
    page_number = 1
    for num_problems in arr:
        for i in range(1, num_problems+1):
            if page_number == i:
                count += 1
            if i % k == 0 and i != num_problems:
                page_number += 1
        page_number += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
