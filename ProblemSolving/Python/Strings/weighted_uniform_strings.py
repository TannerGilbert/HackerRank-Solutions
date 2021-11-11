import os


def weightedUniformStrings(s, queries):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    prev_c = ''
    count = 1
    weights = set()
    for c in s:
        if c == prev_c:
            count += 1
        else:
            count = 1
        prev_c = c
        weights.add((alphabet.index(c) + 1) * count)
    return list(map(lambda x: 'Yes' if x in weights else 'No', queries))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
