import os
import itertools


def minimumDistances(a):
    min_distance = -1
    for value in set(a):
        indices = [i for i, v in enumerate(a) if v == value]
        if len(indices) > 1:
            min_d = min([abs(i1 - i2) for i1, i2 in itertools.permutations(indices, 2)])
            
            if min_d < min_distance or min_distance == -1:
                min_distance = min_d
                
    return min_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
