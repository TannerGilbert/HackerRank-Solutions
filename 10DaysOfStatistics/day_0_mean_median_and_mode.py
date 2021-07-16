import sys
import math
from collections import Counter

num_elements = int(sys.stdin.readline())
elements = [int(i) for i in sys.stdin.readline().split(' ')]
elements.sort()

# calculate mean
mean = round(sum(elements) / num_elements, 1)

# calculate median
median = 0
index = (num_elements - 1) // 2
if num_elements % 2 == 1:
    median = elements[index]
else:
    median = (elements[index] + elements[index + 1]) / 2.0


# calculate mode
c = Counter(elements)
max_count = max(c.values())
mode = min(k for k,v in c.items() if v==max_count)

print(mean)
print(median)
print(mode)