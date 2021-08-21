def insertionSort2(n, arr):
    init_arr = arr.copy()
    for e in arr[1:]:
        for i in range(init_arr.index(e) - 1, -1, -1):
            if arr[i] > e and i == 0:
                arr[i+1] = arr[i]
                arr[i] = e
                break
            elif arr[i] > e:                
                arr[i+1] = arr[i]
            else:
                arr[i+1] = e
                break
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
