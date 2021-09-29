from collections import OrderedDict

ordered_dict = OrderedDict()
N = int(input())

for _ in range(N):
    key = input().strip() 
    if key in ordered_dict:
        ordered_dict[key] += 1
    else:
        ordered_dict[key] = 1

print(len(ordered_dict.values()))
print(*ordered_dict.values())
