import os


def makingAnagrams(s1, s2):
    unique_chars = list(set.union(set(s1), set(s2)))
    count = 0
    for c in unique_chars:
        count += abs(s1.count(c) - s2.count(c))
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
