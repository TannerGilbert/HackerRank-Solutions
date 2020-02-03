if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])
    
    scores = sorted(list(set(scores)))
    second_lowest = []

    for name, score in students:
        if score == scores[1]:
            second_lowest.append(name)
    
    for s in sorted(second_lowest):
        print(s)