def countSort(arr):
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    
    output = [[] for _ in range(n)]
    for e in arr:
        output[int(e[0])].append(e[1])
    print(' '.join(j for i in output for j in i))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
