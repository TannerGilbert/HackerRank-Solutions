def quicksort(start, end):
    global ar
    if end - start > 1:
        a = ar[end-1]
        s = start
        for i in range(start, end):
            if a >= ar[i]:
                ar[s], ar[i] = ar[i], ar[s]
                s += 1
        print(*ar)
        quicksort(start, s-1)
        quicksort(s, end)


n = int(input())
ar = list(map(int, input().split()))

quicksort(0, n)