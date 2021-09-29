from collections import namedtuple

N = int(input())
columns = input()
Student = namedtuple('Student', columns)
marks = [int(Student(*input().split()).MARKS) for _ in range(N)] 
print(sum(marks) / len(marks))
