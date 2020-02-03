if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(set(arr)))
    if len(arr) > 1:
        print(arr[-2])
    else:
        print(arr[0])