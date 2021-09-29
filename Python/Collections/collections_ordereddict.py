from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for i in range(N):
    key, value = input().rsplit(' ', 1)
    if key in ordered_dictionary:
        ordered_dictionary[key] += int(value)
    else:
        ordered_dictionary[key] = int(value)
        
for key, value in ordered_dictionary.items():
    print(key, value)
