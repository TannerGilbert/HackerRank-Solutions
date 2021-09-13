import os


def hackerrankInString(s):
    for c in 'hackerrank':
        try:
            ind = s.index(c)
            s = s[ind+1:]
        except:
            return 'NO'        
    
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
