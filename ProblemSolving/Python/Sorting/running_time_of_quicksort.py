def insertionSort(ar):
    counter = 0
    for j in range(len(ar)):
        for i in range(j, len(ar)):
            if ar[j] > ar[i]:
                counter += 1
    return counter


def quicksort(ar, start, end, counter=0):
    if end - start > 1:
        a = ar[end-1]
        s = start
        for i in range(start, end):
            if a >= ar[i]:
                ar[s], ar[i] = ar[i], ar[s]
                s += 1
                counter += 1
        counter = quicksort(ar, start, s-1, counter)
        counter = quicksort(ar, s, end, counter)
    return counter


n = int(input())
ar = list(map(int, input().split()))
print(insertionSort(ar) - quicksort(ar, 0, n))