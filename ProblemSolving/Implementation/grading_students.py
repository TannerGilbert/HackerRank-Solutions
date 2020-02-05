#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for i, grade in enumerate(grades):
            if (5 - grade % 5) < 3 and grade >= 38:
                grade += 5 - grade % 5
                grades[i] = grade
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
