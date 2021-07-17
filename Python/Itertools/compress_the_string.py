from itertools import groupby

inp = input()

groups = groupby(inp)
for label, group in groups:
    print((len(list(group)), int(label)), end=' ')
