import os


def anagram(s):
    if len(s) % 2 == 1:
        return -1

    s1 = s[:int(len(s) / 2)]
    s2 = s[int(len(s) / 2):]
    unique_chars = list(set(s2))
    count = 0
    for c in unique_chars:
        count += max(s2.count(c) - s1.count(c), 0)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
