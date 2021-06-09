import math
import os
import random
import re
import sys

def breakingRecords(scores):
    min_score, max_score = scores[0], scores[0]
    min_score_count, max_score_count = 0, 0
    for score in scores[1:]:
        if score < min_score:
            min_score = score
            min_score_count += 1
        if score > max_score:
            max_score = score
            max_score_count += 1
    return max_score_count, min_score_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
