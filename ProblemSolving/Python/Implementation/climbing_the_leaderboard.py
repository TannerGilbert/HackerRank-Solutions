import math
import os
import random
import re
import sys

'''
First try. Terminated due to timeout because it's sorting at every step
def climbingLeaderboard(scores, alice):
    rankings = []
    for i in alice:
        scores.append(i)
        rankings.append(sorted(set(scores), reverse=True).index(i) + 1)
    return rankings
'''

def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rankings = []
    n = len(scores)
    for score in alice:
        while (n > index and score >= scores[index]):
            index += 1
        rankings.append(n+1-index) 
    return rankings


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
