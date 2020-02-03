def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('{:.2f}'.format(mean(student_marks[query_name])))
