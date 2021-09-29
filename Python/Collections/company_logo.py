from collections import Counter


if __name__ == '__main__':
    s = input()
    cnts = Counter(sorted(s))
    for v in cnts.most_common(3):
        print(*v)
