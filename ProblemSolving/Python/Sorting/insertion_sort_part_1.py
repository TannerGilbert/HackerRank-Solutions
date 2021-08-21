def insertionSort1(n, arr):
    e = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > e and i == 0:
            arr[i+1] = arr[i]
            print(*arr)
            arr[i] = e
            break
        elif arr[i] > e:                
            arr[i+1] = arr[i]
        else:
            arr[i+1] = e
            break
        print(*arr)
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
