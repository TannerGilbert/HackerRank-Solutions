import os


def funnyString(s):
    s_rev = s[::-1]

    l1 = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
    l2 = [abs(ord(s_rev[i]) - ord(s_rev[i+1])) for i in range(len(s_rev)-1)]
    
    
    if l1 == l2:
        return 'Funny'
    return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
