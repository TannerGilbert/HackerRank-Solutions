import os


def gemstones(arr):
    unique_chars = list(set(''.join(arr)))
    count = len(unique_chars)
    for c in unique_chars:
        for el in arr:
            if c not in el:
                count -= 1
                break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
