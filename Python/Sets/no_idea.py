arr_len, set_len = map(int, input().split())
arr = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

happiness = 0

for i in arr:
    if i in set1:
        happiness += 1

    if i in set2:
        happiness -= 1

print(happiness)
